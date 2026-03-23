from collections.abc import Callable

from app.tools.base import Tool
from app.tools.contracts import MemoryRepository
from app.tools.impl.memory_repository import default_memory_repository_factory


class ListFilesTool(Tool):
    name = "list_files"
    usage_line = "list_files()"

    def __init__(self, repo_factory: Callable[[], MemoryRepository] | None = None) -> None:
        self._repo_factory = repo_factory or default_memory_repository_factory

    def execute(self, argument: str) -> str:
        return self._repo_factory().list_files(argument)


class ReadFileTool(Tool):
    name = "read_file"
    usage_line = "read_file(nome)"

    def __init__(self, repo_factory: Callable[[], MemoryRepository] | None = None) -> None:
        self._repo_factory = repo_factory or default_memory_repository_factory

    def execute(self, argument: str) -> str:
        return self._repo_factory().read_file(argument)


class SearchMemoryTool(Tool):
    name = "search_memory"
    usage_line = "search_memory(query)"

    def __init__(self, repo_factory: Callable[[], MemoryRepository] | None = None) -> None:
        self._repo_factory = repo_factory or default_memory_repository_factory

    def execute(self, argument: str) -> str:
        return self._repo_factory().search_memory(argument)


class SearchMemoryAllTermsTool(Tool):
    name = "search_memory_all_terms"
    usage_line = "search_memory_all_terms(palavras separadas por espaço)"

    def __init__(self, repo_factory: Callable[[], MemoryRepository] | None = None) -> None:
        self._repo_factory = repo_factory or default_memory_repository_factory

    def execute(self, argument: str) -> str:
        return self._repo_factory().search_memory_all_terms(argument)


class SearchMemoryBm25Tool(Tool):
    name = "search_memory_bm25"
    usage_line = "search_memory_bm25(query) — ranqueia arquivos por BM25 (termos, não frase exata)"

    def __init__(self, repo_factory: Callable[[], MemoryRepository] | None = None) -> None:
        self._repo_factory = repo_factory or default_memory_repository_factory

    def execute(self, argument: str) -> str:
        return self._repo_factory().search_memory_bm25(argument)


class SearchMemoryAllTermsBm25Tool(Tool):
    name = "search_memory_all_terms_bm25"
    usage_line = (
        "search_memory_all_terms_bm25(palavras separadas por espaço) — todos os termos (substring) "
        "e ranqueamento BM25"
    )

    def __init__(self, repo_factory: Callable[[], MemoryRepository] | None = None) -> None:
        self._repo_factory = repo_factory or default_memory_repository_factory

    def execute(self, argument: str) -> str:
        return self._repo_factory().search_memory_all_terms_bm25(argument)


class GrepMemoryTool(Tool):
    name = "grep_memory"
    usage_line = "grep_memory(regex)"

    def __init__(self, repo_factory: Callable[[], MemoryRepository] | None = None) -> None:
        self._repo_factory = repo_factory or default_memory_repository_factory

    def execute(self, argument: str) -> str:
        return self._repo_factory().grep_memory(argument)


class MemoryStatsTool(Tool):
    name = "memory_stats"
    usage_line = "memory_stats()"

    def __init__(self, repo_factory: Callable[[], MemoryRepository] | None = None) -> None:
        self._repo_factory = repo_factory or default_memory_repository_factory

    def execute(self, argument: str) -> str:
        return self._repo_factory().memory_stats(argument)


class MemoryTocTool(Tool):
    name = "memory_toc"
    usage_line = "memory_toc(nome_arquivo_md)"

    def __init__(self, repo_factory: Callable[[], MemoryRepository] | None = None) -> None:
        self._repo_factory = repo_factory or default_memory_repository_factory

    def execute(self, argument: str) -> str:
        return self._repo_factory().memory_toc(argument)
