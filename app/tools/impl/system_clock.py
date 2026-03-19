from datetime import datetime

from app.tools.contracts import Clock


class SystemClock(Clock):
    """Default wall-clock implementation."""

    def now_iso(self) -> str:
        return datetime.now().astimezone().isoformat(timespec="seconds")


def default_clock_factory() -> Clock:
    return SystemClock()
