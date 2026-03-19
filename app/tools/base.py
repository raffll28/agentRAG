from abc import ABC, abstractmethod
from typing import ClassVar


class Tool(ABC):
    """Strategy interface: each concrete tool implements a single capability."""

    name: ClassVar[str]
    usage_line: ClassVar[str]

    @abstractmethod
    def execute(self, argument: str) -> str:
        """Run the tool; `argument` is the LLM-provided input line (may be empty)."""
        raise NotImplementedError
