import os
import re
from pathlib import Path

from app.settings import get_settings
from app.tools.contracts import MemoryRepository

MAX_GREP_PATTERN_LEN = 256
MAX_GREP_MATCH_LINES = 80
MAX_GREP_FILE_BYTES = 512 * 1024


def _memory_dir() -> Path:
    return Path(__file__).resolve().parents[2] / "memory"


def default_memory_repository_factory() -> MemoryRepository:
    """Builds a repository rooted at the default app/memory path (re-evaluated each call for tests)."""
    return FilesystemMemoryRepository(_memory_dir())


def _read_bytes_capped(path: Path, max_bytes: int) -> tuple[bytes, bool]:
    with path.open("rb") as f:
        data = f.read(max_bytes + 1)
    if len(data) > max_bytes:
        return data[:max_bytes], True
    return data, False


def _bytes_to_text(data: bytes) -> str:
    return data.decode("utf-8", errors="replace")


def _snippet_around(text: str, needle: str, max_len: int) -> str:
    if max_len < 50:
        max_len = 50
    if not needle.strip():
        body = text[:max_len]
        return body + ("…" if len(text) > max_len else "")
    lower = text.lower()
    n = needle.lower()
    idx = lower.find(n)
    if idx < 0:
        body = text[:max_len]
        return body + ("…" if len(text) > max_len else "")
    radius = max_len // 2
    start = max(0, idx - radius)
    end = min(len(text), start + max_len)
    start = max(0, end - max_len)
    out = text[start:end]
    prefix = "…" if start > 0 else ""
    suffix = "…" if end < len(text) else ""
    return prefix + out + suffix


def _terms_in_text(terms: list[str], text: str) -> bool:
    lower = text.lower()
    return all(t in lower for t in terms)


class FilesystemMemoryRepository(MemoryRepository):
    """Adapter: memory as UTF-8 files under a single directory (Repository pattern)."""

    def __init__(self, root: Path) -> None:
        self._root = root

    def _is_safe_memory_filename(self, name: str) -> bool:
        s = name.strip()
        if not s or s in (".", ".."):
            return False
        if "/" in s or "\\" in s or "\x00" in s:
            return False
        base = self._root.resolve()
        try:
            candidate = (base / s).resolve()
            candidate.relative_to(base)
        except (OSError, ValueError):
            return False
        return candidate.name == Path(s).name

    def _memory_file_path(self, filename: str) -> Path | None:
        if not self._is_safe_memory_filename(filename):
            return None
        p = (self._root / filename.strip()).resolve()
        return p if p.is_file() else None

    def list_files(self, _argument: str) -> str:
        path = self._root
        if not path.is_dir():
            return "Diretório de memória não encontrado"
        names = sorted(os.listdir(path))
        return ", ".join(names) if names else "(vazio)"

    def read_file(self, filename: str) -> str:
        path = self._memory_file_path(filename)
        if path is None:
            return "Arquivo não encontrado"

        settings = get_settings()
        max_chars = settings.read_file_max_chars
        max_bytes = max_chars * 4
        try:
            raw, truncated = _read_bytes_capped(path, max_bytes)
        except OSError:
            return "Erro ao ler arquivo"
        text = _bytes_to_text(raw)
        if len(text) > max_chars:
            text = text[:max_chars]
            truncated = True
        if truncated:
            return (
                text
                + "\n\n[Conteúdo truncado por limite READ_FILE_MAX_CHARS; "
                "peça seções menores ou use memory_toc.]"
            )
        return text

    def search_memory(self, query: str) -> str:
        path = self._root
        if not path.is_dir():
            return "Diretório de memória não encontrado"

        settings = get_settings()
        max_scan = settings.memory_max_bytes_per_file_search
        snip = settings.memory_search_snippet_chars
        max_total = settings.memory_search_max_total_chars

        chunks: list[str] = []
        total = 0

        for name in os.listdir(path):
            file_path = path / name
            if not file_path.is_file():
                continue
            try:
                raw, truncated = _read_bytes_capped(file_path, max_scan)
            except OSError:
                continue
            text = _bytes_to_text(raw)
            if query.lower() not in text.lower():
                continue
            body = _snippet_around(text, query, snip)
            note = ""
            if truncated:
                note = "\n[Nota: busca só considerou o início do arquivo; use read_file para o arquivo completo.]"
            block = f"Arquivo: {name}\n{body}{note}"
            sep_len = 2 if chunks else 0
            if total + sep_len + len(block) > max_total:
                chunks.append(
                    "\n\n[Resultado total truncado por MEMORY_SEARCH_MAX_TOTAL_CHARS. Refine a consulta.]"
                )
                break
            chunks.append(("\n\n" if chunks else "") + block)
            total += sep_len + len(block)

        return "".join(chunks).strip() if chunks else "Nada encontrado"

    def search_memory_all_terms(self, query: str) -> str:
        path = self._root
        if not path.is_dir():
            return "Diretório de memória não encontrado"

        terms = [t.lower() for t in query.split() if t.strip()]
        if not terms:
            return "Informe ao menos uma palavra"

        settings = get_settings()
        max_scan = settings.memory_max_bytes_per_file_search
        snip = settings.memory_search_snippet_chars
        max_total = settings.memory_search_max_total_chars

        chunks: list[str] = []
        total = 0

        for name in os.listdir(path):
            file_path = path / name
            if not file_path.is_file():
                continue
            try:
                raw, truncated = _read_bytes_capped(file_path, max_scan)
            except OSError:
                continue
            text = _bytes_to_text(raw)
            if not _terms_in_text(terms, text):
                continue
            body = _snippet_around(text, terms[0], snip)
            note = ""
            if truncated:
                note = (
                    "\n[Nota: correspondência verificada só no início do arquivo; "
                    "termos distantes no fim podem não aparecer — use read_file se necessário.]"
                )
            block = f"Arquivo: {name}\n{body}{note}"
            sep_len = 2 if chunks else 0
            if total + sep_len + len(block) > max_total:
                chunks.append(
                    "\n\n[Resultado total truncado por MEMORY_SEARCH_MAX_TOTAL_CHARS. Refine a consulta.]"
                )
                break
            chunks.append(("\n\n" if chunks else "") + block)
            total += sep_len + len(block)

        return "".join(chunks).strip() if chunks else "Nada encontrado"

    def grep_memory(self, pattern: str) -> str:
        raw = pattern.strip()
        if not raw:
            return "Informe um padrão regex"
        if len(raw) > MAX_GREP_PATTERN_LEN:
            return f"Padrão muito longo (máx {MAX_GREP_PATTERN_LEN} caracteres)"

        try:
            regex = re.compile(raw, re.IGNORECASE | re.MULTILINE)
        except re.error as e:
            return f"Regex inválida: {e}"

        base = self._root
        if not base.is_dir():
            return "Diretório de memória não encontrado"

        lines_out: list[str] = []
        for name in sorted(os.listdir(base)):
            file_path = base / name
            if not file_path.is_file():
                continue
            try:
                data = file_path.read_bytes()
            except OSError:
                continue
            if len(data) > MAX_GREP_FILE_BYTES:
                data = data[:MAX_GREP_FILE_BYTES]
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                text = data.decode("utf-8", errors="replace")

            for lineno, line in enumerate(text.splitlines(), start=1):
                if regex.search(line):
                    lines_out.append(f"{name}:{lineno}:{line.rstrip()}")
                    if len(lines_out) >= MAX_GREP_MATCH_LINES:
                        break
            if len(lines_out) >= MAX_GREP_MATCH_LINES:
                break

        if not lines_out:
            return "Nenhuma linha encontrada"
        suffix = "\n… (limite de linhas atingido)" if len(lines_out) >= MAX_GREP_MATCH_LINES else ""
        return "\n".join(lines_out) + suffix

    def memory_stats(self, _argument: str) -> str:
        base = self._root
        if not base.is_dir():
            return "Diretório de memória não encontrado"

        rows: list[str] = []
        for name in sorted(os.listdir(base)):
            p = base / name
            if not p.is_file():
                continue
            try:
                st = p.stat()
            except OSError:
                continue
            mtime = int(st.st_mtime)
            rows.append(f"{name}\tsize_bytes={st.st_size}\tmtime_unix={mtime}")

        return "\n".join(rows) if rows else "(nenhum arquivo)"

    _HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$")

    def memory_toc(self, filename: str) -> str:
        path = self._memory_file_path(filename)
        if path is None:
            return "Arquivo não encontrado"

        if path.suffix.lower() != ".md":
            return "Suportado apenas para arquivos .md"

        settings = get_settings()
        max_bytes = min(settings.read_file_max_chars * 4, 2 * 1024 * 1024)

        lines_out: list[str] = []
        try:
            raw, truncated = _read_bytes_capped(path, max_bytes)
        except OSError:
            return "Erro ao ler arquivo"
        text = _bytes_to_text(raw)
        for lineno, line in enumerate(text.splitlines(), start=1):
            m = self._HEADING_RE.match(line)
            if m:
                level = len(m.group(1))
                title = m.group(2)
                indent = "  " * (level - 1)
                lines_out.append(f"L{lineno}: {indent}{title}")
        if truncated:
            lines_out.append("[TOC parcial: arquivo truncado na leitura.]")
        return "\n".join(lines_out) if lines_out else "(sem headings # no arquivo)"
