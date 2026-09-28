from core.planner import Planner
from core.types import (
    Intent,
    IntentType,
)


def test_app_plan():

    planner = Planner()

    intent = Intent(
        type=IntentType.APP_OPERATION,
        action="open",
        target="Chrome",
    )

    plan = planner.create_plan(intent)

    assert len(plan.steps) == 1

    step = plan.steps[0]

    assert step.tool == "apps"
    assert step.action == "open"
    assert step.parameters["app"] == "Chrome"