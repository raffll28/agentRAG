import os
from dataclasses import dataclass


def _int_env(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        return max(0, int(raw))
    except ValueError:
        return default


@dataclass(frozen=True)
class Settings:
    """Runtime limits for scalability (overridable via environment)."""

    agent_max_concurrent: int
    agent_max_prompt_chars: int
    memory_max_bytes_per_file_search: int
    memory_search_snippet_chars: int
    memory_search_max_total_chars: int
    read_file_max_chars: int


def get_settings() -> Settings:
    return Settings(
        agent_max_concurrent=max(1, _int_env("AGENT_MAX_CONCURRENT", 4)),
        agent_max_prompt_chars=max(4096, _int_env("AGENT_MAX_PROMPT_CHARS", 28_000)),
        memory_max_bytes_per_file_search=max(
            4096, _int_env("MEMORY_MAX_BYTES_PER_FILE_SEARCH", 512 * 1024)
        ),
        memory_search_snippet_chars=max(200, _int_env("MEMORY_SEARCH_SNIPPET_CHARS", 4_000)),
        memory_search_max_total_chars=max(
            2000, _int_env("MEMORY_SEARCH_MAX_TOTAL_CHARS", 48_000)
        ),
        read_file_max_chars=max(4096, _int_env("READ_FILE_MAX_CHARS", 200_000)),
    )
