from app.tools.base import Tool
from app.tools.impl.memory_tools import (
    GrepMemoryTool,
    ListFilesTool,
    MemoryStatsTool,
    MemoryTocTool,
    ReadFileTool,
    SearchMemoryAllTermsTool,
    SearchMemoryTool,
)
from app.tools.impl.system_tools import GetCurrentDatetimeTool


class ToolRegistry:
    """Registry pattern: map tool name to a Tool instance and dispatch execution."""

    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def run(self, name: str, argument: str) -> str:
        tool = self._tools.get(name.strip())
        if tool is None:
            return "Tool desconhecida"
        return tool.execute(argument)

    def list_names(self) -> list[str]:
        return sorted(self._tools.keys())

    def format_usage_lines_for_prompt(self) -> str:
        ordered = sorted(self._tools.values(), key=lambda t: t.name)
        return "\n".join(f"- {t.usage_line}" for t in ordered)


def _default_tools() -> tuple[Tool, ...]:
    return (
        GetCurrentDatetimeTool(),
        GrepMemoryTool(),
        ListFilesTool(),
        MemoryStatsTool(),
        MemoryTocTool(),
        ReadFileTool(),
        SearchMemoryAllTermsTool(),
        SearchMemoryTool(),
    )


def build_default_registry() -> ToolRegistry:
    registry = ToolRegistry()
    for tool in _default_tools():
        registry.register(tool)
    return registry


_default_registry = build_default_registry()


def run_tool(name: str, argument: str) -> str:
    return _default_registry.run(name, argument)


def list_tool_names() -> list[str]:
    return _default_registry.list_names()


def default_tool_usage_block() -> str:
    return _default_registry.format_usage_lines_for_prompt()
