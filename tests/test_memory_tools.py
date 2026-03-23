from app.tools.impl import memory_repository as memory_repo
from app.tools.impl.memory_repository import FilesystemMemoryRepository
from app.tools.registry import run_tool


def test_list_files_empty_dir(tmp_path):
    repo = FilesystemMemoryRepository(tmp_path)
    assert repo.list_files("") == "(vazio)"


def test_read_file_and_search_memory(tmp_path):
    repo = FilesystemMemoryRepository(tmp_path)
    tmp_path.joinpath("notes.txt").write_text("alpha beta", encoding="utf-8")

    assert repo.read_file("notes.txt") == "alpha beta"
    assert "alpha" in repo.search_memory("beta")
    assert repo.search_memory("zzz") == "Nada encontrado"
    assert repo.read_file("missing.txt") == "Arquivo não encontrado"


def test_run_tool_delegates_to_memory_with_patched_dir(monkeypatch, tmp_path):
    monkeypatch.setattr(memory_repo, "_memory_dir", lambda: tmp_path)
    tmp_path.joinpath("x.md").write_text("hello", encoding="utf-8")

    assert run_tool("read_file", "x.md") == "hello"
    assert "hello" in run_tool("search_memory", "ello")


def test_read_file_rejects_unsafe_paths(tmp_path):
    repo = FilesystemMemoryRepository(tmp_path)
    tmp_path.joinpath("safe.txt").write_text("ok", encoding="utf-8")
    assert repo.read_file("safe.txt") == "ok"
    assert repo.read_file("../evil.txt") == "Arquivo não encontrado"
    assert repo.read_file("a/b.txt") == "Arquivo não encontrado"


def test_search_memory_all_terms(tmp_path):
    repo = FilesystemMemoryRepository(tmp_path)
    tmp_path.joinpath("doc.md").write_text("alpha beta gamma", encoding="utf-8")
    assert "alpha" in repo.search_memory_all_terms("alpha gamma")
    assert repo.search_memory_all_terms("alpha zzz") == "Nada encontrado"
    assert repo.search_memory_all_terms("   ") == "Informe ao menos uma palavra"


def test_search_memory_bm25_ranks_by_term_frequency(tmp_path):
    repo = FilesystemMemoryRepository(tmp_path)
    tmp_path.joinpath("noise.md").write_text("lorem ipsum dolor", encoding="utf-8")
    tmp_path.joinpath("sparse.md").write_text("python is nice", encoding="utf-8")
    tmp_path.joinpath("dense.md").write_text(
        "python python python programming", encoding="utf-8"
    )
    out = repo.search_memory_bm25("python")
    assert "dense.md" in out and "sparse.md" in out
    assert "noise.md" not in out
    assert out.index("dense.md") < out.index("sparse.md")


def test_search_memory_bm25_empty_query(tmp_path):
    repo = FilesystemMemoryRepository(tmp_path)
    tmp_path.joinpath("a.md").write_text("word", encoding="utf-8")
    assert "termo" in repo.search_memory_bm25("   ").lower()


def test_search_memory_all_terms_bm25(tmp_path):
    repo = FilesystemMemoryRepository(tmp_path)
    tmp_path.joinpath("doc.md").write_text("alpha beta gamma delta", encoding="utf-8")
    assert "alpha" in repo.search_memory_all_terms_bm25("alpha gamma")
    assert repo.search_memory_all_terms_bm25("alpha zzz") == "Nada encontrado"
    assert repo.search_memory_all_terms_bm25("   ") == "Informe ao menos uma palavra"


def test_run_tool_search_memory_bm25(monkeypatch, tmp_path):
    monkeypatch.setattr(memory_repo, "_memory_dir", lambda: tmp_path)
    tmp_path.joinpath("z.md").write_text("lorem ipsum", encoding="utf-8")
    tmp_path.joinpath("x.md").write_text("rust rust rust", encoding="utf-8")
    tmp_path.joinpath("y.md").write_text("rust once", encoding="utf-8")
    out = run_tool("search_memory_bm25", "rust")
    assert "x.md" in out and "y.md" in out
    assert "z.md" not in out
    assert out.index("x.md") < out.index("y.md")


def test_grep_memory(tmp_path):
    repo = FilesystemMemoryRepository(tmp_path)
    tmp_path.joinpath("log.txt").write_text("line one\nLINE two\n", encoding="utf-8")
    out = repo.grep_memory(r"(?i)^line")
    assert "log.txt:1" in out
    assert "log.txt:2" in out
    assert "Regex inválida" in repo.grep_memory("[bad")


def test_memory_stats(tmp_path):
    repo = FilesystemMemoryRepository(tmp_path)
    tmp_path.joinpath("z.md").write_text("x", encoding="utf-8")
    out = repo.memory_stats("")
    assert "z.md" in out and "size_bytes=" in out


def test_memory_toc(tmp_path):
    repo = FilesystemMemoryRepository(tmp_path)
    tmp_path.joinpath("h.md").write_text("# Title\n## Sub\nplain\n", encoding="utf-8")
    out = repo.memory_toc("h.md")
    assert "Title" in out and "Sub" in out
    assert repo.memory_toc("nope.md") == "Arquivo não encontrado"


def test_get_current_datetime_tool():
    out = run_tool("get_current_datetime", "")
    assert len(out) >= 19
    assert "T" in out
