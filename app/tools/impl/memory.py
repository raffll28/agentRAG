import os
from pathlib import Path


def _memory_dir() -> Path:
    return Path(__file__).resolve().parents[2] / "memory"


def list_files(_argument: str) -> str:
    path = _memory_dir()
    if not path.is_dir():
        return "Diretório de memória não encontrado"
    names = sorted(os.listdir(path))
    return ", ".join(names) if names else "(vazio)"


def read_file(filename: str) -> str:
    path = _memory_dir() / filename
    if not path.is_file():
        return "Arquivo não encontrado"

    with path.open(encoding="utf-8") as f:
        return f.read()


def search_memory(query: str) -> str:
    path = _memory_dir()
    if not path.is_dir():
        return "Diretório de memória não encontrado"

    results = []
    for name in os.listdir(path):
        file_path = path / name
        if not file_path.is_file():
            continue
        content = file_path.read_text(encoding="utf-8")
        if query.lower() in content.lower():
            results.append(f"Arquivo: {name}\n{content}")

    return "\n\n".join(results) if results else "Nada encontrado"
