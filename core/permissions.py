from .types import (
    PermissionDecision,
    PermissionLevel,
    PlanStep,
)


class PermissionManager:

    CONFIRM_ACTIONS = {
        "delete",
        "send_message",
        "shutdown",
        "restart",
        "install",
    }

    def check(self, step: PlanStep) -> PermissionDecision:

        if step.action in self.CONFIRM_ACTIONS:
            return PermissionDecision(
                level=PermissionLevel.CONFIRM,
                reason=f"Action '{step.action}' requires confirmation.",
                approved=False,
            )

        if step.permission == PermissionLevel.DENY:
            return PermissionDecision(
                level=PermissionLevel.DENY,
                reason="Action is explicitly denied.",
                approved=False,
            )

        return PermissionDecision(
            level=PermissionLevel.SAFE,
            reason="Action is considered safe.",
            approved=True,
        )