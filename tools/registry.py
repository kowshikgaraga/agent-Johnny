from collections.abc import Callable
from typing import Any


class ToolRegistry:

    def __init__(self):
        self._tools: dict[str, dict[str, Callable[..., Any]]] = {}

    def register(
        self,
        tool_name: str,
        action: str,
        handler: Callable[..., Any],
    ) -> None:
        self._tools.setdefault(tool_name, {})
        self._tools[tool_name][action] = handler

    def execute(
        self,
        tool_name: str,
        action: str,
        parameters: dict[str, Any],
    ) -> Any:

        if tool_name not in self._tools:
            raise ValueError(f"Unknown tool: {tool_name}")

        if action not in self._tools[tool_name]:
            raise ValueError(
                f"Unknown action '{action}' "
                f"for tool '{tool_name}'"
            )

        handler = self._tools[tool_name][action]

        return handler(**parameters)