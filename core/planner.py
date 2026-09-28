from .types import (
    Intent,
    IntentType,
    PermissionLevel,
    Plan,
    PlanStep,
)


class Planner:

    def create_plan(self, intent: Intent) -> Plan:

        if intent.type == IntentType.APP_OPERATION:
            return Plan(
                steps=[
                    PlanStep(
                        id="step-1",
                        tool="apps",
                        action=intent.action,
                        parameters={
                            "app": intent.target,
                        },
                        permission=PermissionLevel.SAFE,
                    )
                ]
            )

        if intent.type == IntentType.FILE_OPERATION:
            return Plan(
                steps=[
                    PlanStep(
                        id="step-1",
                        tool="files",
                        action="search",
                        parameters=intent.parameters,
                        permission=PermissionLevel.SAFE,
                    )
                ]
            )

        return Plan()