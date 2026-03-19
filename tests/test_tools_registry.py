from app.tools import default_tool_usage_block, list_tool_names, run_tool


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
    }


def test_run_tool_unknown():
    assert run_tool("nonexistent_tool", "") == "Tool desconhecida"


def test_run_tool_list_files_uses_project_memory():
    out = run_tool("list_files", "")
    assert "hardware.md" in out
