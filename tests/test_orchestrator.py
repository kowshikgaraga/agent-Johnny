from core.intent import IntentDetector
from core.orchestrator import Orchestrator
from core.permissions import PermissionManager
from core.planner import Planner
from tools.registry import ToolRegistry


def test_orchestrator_executes_app_action():

    registry = ToolRegistry()

    registry.register(
        "apps",
        "open",
        lambda app: f"opened {app}",
    )

    orchestrator = Orchestrator(
        intent_detector=IntentDetector(),
        planner=Planner(),
        permissions=PermissionManager(),
        tools=registry,
    )

    result = orchestrator.handle("Open Chrome")

    assert result.success is True
    assert result.data == ["opened Chrome"]