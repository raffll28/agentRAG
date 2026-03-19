"""Structural interfaces (Protocol) for tool dependencies — dependency inversion."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class MemoryRepository(Protocol):
    """Port for agent memory stored as files (RAG source documents)."""

    def list_files(self, argument: str) -> str: ...

    def read_file(self, filename: str) -> str: ...

    def search_memory(self, query: str) -> str: ...

    def search_memory_all_terms(self, query: str) -> str: ...

    def grep_memory(self, pattern: str) -> str: ...

    def memory_stats(self, argument: str) -> str: ...

    def memory_toc(self, filename: str) -> str: ...


@runtime_checkable
class Clock(Protocol):
    """Port for time readings (injectable for tests)."""

    def now_iso(self) -> str: ...
