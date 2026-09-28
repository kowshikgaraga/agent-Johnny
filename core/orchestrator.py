from .intent import IntentDetector
from .permissions import PermissionManager
from .planner import Planner
from .types import (
    ExecutionResult,
    UserRequest,
)
from tools.registry import ToolRegistry


class Orchestrator:

    def __init__(
        self,
        intent_detector: IntentDetector,
        planner: Planner,
        permissions: PermissionManager,
        tools: ToolRegistry,
    ):
        self.intent_detector = intent_detector
        self.planner = planner
        self.permissions = permissions
        self.tools = tools

    def handle(self, text: str) -> ExecutionResult:

        request = UserRequest(text=text)

        # 1. Understand request
        intent = self.intent_detector.detect(request)

        # 2. Create execution plan
        plan = self.planner.create_plan(intent)

        if not plan.steps:
            return ExecutionResult(
                success=False,
                message="I don't know how to execute that request.",
            )

        results = []

        # 3. Validate + execute
        for step in plan.steps:

            decision = self.permissions.check(step)

            if not decision.approved:
                return ExecutionResult(
                    success=False,
                    message=decision.reason,
                )

            try:
                result = self.tools.execute(
                    tool_name=step.tool,
                    action=step.action,
                    parameters=step.parameters,
                )

                results.append(result)

            except Exception as exc:
                return ExecutionResult(
                    success=False,
                    message="Tool execution failed.",
                    error=str(exc),
                )

        return ExecutionResult(
            success=True,
            message="Request executed successfully.",
            data=results,
        )