from abc import ABC, abstractmethod
from typing import ClassVar


class Tool(ABC):
    """Nominal Strategy contract for the agent registry (see `contracts` for dependency ports)."""

    name: ClassVar[str]
    usage_line: ClassVar[str]

    @abstractmethod
    def execute(self, argument: str) -> str:
        """Run the tool; `argument` is the LLM-provided input line (may be empty)."""
        raise NotImplementedError
