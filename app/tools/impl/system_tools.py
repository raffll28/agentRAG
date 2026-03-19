from collections.abc import Callable

from app.tools.base import Tool
from app.tools.contracts import Clock
from app.tools.impl.system_clock import default_clock_factory


class GetCurrentDatetimeTool(Tool):
    name = "get_current_datetime"
    usage_line = "get_current_datetime()"

    def __init__(self, clock_factory: Callable[[], Clock] | None = None) -> None:
        self._clock_factory = clock_factory or default_clock_factory

    def execute(self, argument: str) -> str:
        return self._clock_factory().now_iso()
