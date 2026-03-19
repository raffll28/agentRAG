from app.tools.impl import memory as memory_mod
from app.tools.registry import run_tool


def test_list_files_empty_dir(monkeypatch, tmp_path):
    monkeypatch.setattr(memory_mod, "_memory_dir", lambda: tmp_path)
    assert memory_mod.list_files("") == "(vazio)"


def test_read_file_and_search_memory(monkeypatch, tmp_path):
    monkeypatch.setattr(memory_mod, "_memory_dir", lambda: tmp_path)
    tmp_path.joinpath("notes.txt").write_text("alpha beta", encoding="utf-8")

    assert memory_mod.read_file("notes.txt") == "alpha beta"
    assert "alpha" in memory_mod.search_memory("beta")
    assert memory_mod.search_memory("zzz") == "Nada encontrado"
    assert memory_mod.read_file("missing.txt") == "Arquivo não encontrado"


def test_run_tool_delegates_to_memory_with_patched_dir(monkeypatch, tmp_path):
    monkeypatch.setattr(memory_mod, "_memory_dir", lambda: tmp_path)
    tmp_path.joinpath("x.md").write_text("hello", encoding="utf-8")

    assert run_tool("read_file", "x.md") == "hello"
    assert "hello" in run_tool("search_memory", "ello")
