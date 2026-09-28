from core.permissions import PermissionManager
from core.types import (
    PermissionLevel,
    PlanStep,
)


def test_safe_action():

    manager = PermissionManager()

    step = PlanStep(
        id="1",
        tool="apps",
        action="open",
        permission=PermissionLevel.SAFE,
    )

    decision = manager.check(step)

    assert decision.approved is True


def test_delete_requires_confirmation():

    manager = PermissionManager()

    step = PlanStep(
        id="1",
        tool="files",
        action="delete",
        permission=PermissionLevel.CONFIRM,
    )

    decision = manager.check(step)

    assert decision.approved is False
    assert decision.level == PermissionLevel.CONFIRM