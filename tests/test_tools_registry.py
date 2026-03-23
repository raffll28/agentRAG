from app.tools import default_tool_usage_block, list_tool_names, run_tool
from app.tools.impl import memory_repository as memory_repo


def test_default_tool_usage_block_lists_all_tools():
    block = default_tool_usage_block()
    for name in list_tool_names():
        assert name in block


def test_list_tool_names_sorted():
    names = list_tool_names()
    assert names == sorted(names)
    assert set(names) == {
        "get_current_datetime",
        "grep_memory",
        "list_files",
        "memory_stats",
        "memory_toc",
        "read_file",
        "search_memory",
        "search_memory_all_terms",
        "search_memory_all_terms_bm25",
        "search_memory_bm25",
    }


def test_run_tool_unknown():
    assert run_tool("nonexistent_tool", "") == "Tool desconhecida"


def test_run_tool_list_files_uses_project_memory(monkeypatch, tmp_path):
    monkeypatch.setattr(memory_repo, "_memory_dir", lambda: tmp_path)
    tmp_path.joinpath("hardware.md").write_text("# stub", encoding="utf-8")
    out = run_tool("list_files", "")
    assert "hardware.md" in out
