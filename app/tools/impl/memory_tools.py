from app.tools.base import Tool
from app.tools.impl import memory as memory_mod


class ListFilesTool(Tool):
    name = "list_files"
    usage_line = "list_files()"

    def execute(self, argument: str) -> str:
        return memory_mod.list_files(argument)


class ReadFileTool(Tool):
    name = "read_file"
    usage_line = "read_file(nome)"

    def execute(self, argument: str) -> str:
        return memory_mod.read_file(argument)


class SearchMemoryTool(Tool):
    name = "search_memory"
    usage_line = "search_memory(query)"

    def execute(self, argument: str) -> str:
        return memory_mod.search_memory(argument)
