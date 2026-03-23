import app.agent as agent_mod
from app.settings import Settings


def test_truncate_llm_prompt_inserts_marker(monkeypatch):
    monkeypatch.setattr(
        agent_mod,
        "get_settings",
        lambda: Settings(
            agent_max_concurrent=4,
            agent_max_prompt_chars=5_000,
            memory_max_bytes_per_file_search=512 * 1024,
            memory_search_snippet_chars=4_000,
            memory_search_max_total_chars=48_000,
            read_file_max_chars=200_000,
        ),
    )
    huge = "x" * 20_000
    out = agent_mod._truncate_llm_prompt(huge)
    assert len(out) <= 6_000
    assert "omitido" in out
    assert huge[-200:] in out


def test_search_memory_respects_total_cap(monkeypatch, tmp_path):
    from app.tools.impl.memory_repository import FilesystemMemoryRepository

    monkeypatch.setattr(
        "app.tools.impl.memory_repository.get_settings",
        lambda: Settings(
            agent_max_concurrent=4,
            agent_max_prompt_chars=28_000,
            memory_max_bytes_per_file_search=512 * 1024,
            memory_search_snippet_chars=100,
            memory_search_max_total_chars=120,
            read_file_max_chars=200_000,
        ),
    )
    repo = FilesystemMemoryRepository(tmp_path)
    for i in range(3):
        tmp_path.joinpath(f"f{i}.md").write_text(f"hit {i} " + "y" * 80, encoding="utf-8")
    out = repo.search_memory("hit")
    assert "truncado" in out.lower() or "MEMORY_SEARCH_MAX_TOTAL" in out


def test_search_memory_bm25_respects_total_cap(monkeypatch, tmp_path):
    from app.tools.impl.memory_repository import FilesystemMemoryRepository

    monkeypatch.setattr(
        "app.tools.impl.memory_repository.get_settings",
        lambda: Settings(
            agent_max_concurrent=4,
            agent_max_prompt_chars=28_000,
            memory_max_bytes_per_file_search=512 * 1024,
            memory_search_snippet_chars=100,
            memory_search_max_total_chars=120,
            read_file_max_chars=200_000,
        ),
    )
    repo = FilesystemMemoryRepository(tmp_path)
    for i in range(3):
        tmp_path.joinpath(f"f{i}.md").write_text(f"hit {i} " + "y" * 80, encoding="utf-8")
    out = repo.search_memory_bm25("hit")
    assert "truncado" in out.lower() or "MEMORY_SEARCH_MAX_TOTAL" in out
