from core.intent import IntentDetector
from core.orchestrator import Orchestrator
from core.permissions import PermissionManager
from core.planner import Planner

from tools.apps import AppTool
from tools.files import FileTool
from tools.registry import ToolRegistry


def build_orchestrator() -> Orchestrator:

    registry = ToolRegistry()

    apps = AppTool()
    files = FileTool()

    registry.register(
        "apps",
        "open",
        apps.open,
    )

    registry.register(
        "apps",
        "close",
        apps.close,
    )

    registry.register(
        "files",
        "search",
        files.search,
    )

    return Orchestrator(
        intent_detector=IntentDetector(),
        planner=Planner(),
        permissions=PermissionManager(),
        tools=registry,
    )


if __name__ == "__main__":

    orchestrator = build_orchestrator()

    while True:
        user_input = input("You: ")

        if user_input.lower() in {"exit", "quit"}:
            break

        result = orchestrator.handle(user_input)

        print(result.message)

        if result.data:
            print(result.data)