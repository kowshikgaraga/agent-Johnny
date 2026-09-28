from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class IntentType(str, Enum):
    CHAT = "chat"
    QUESTION = "question"
    FILE_OPERATION = "file_operation"
    APP_OPERATION = "app_operation"
    SYSTEM_OPERATION = "system_operation"
    BROWSER_OPERATION = "browser_operation"
    SEARCH = "search"
    UNKNOWN = "unknown"


class PermissionLevel(str, Enum):
    SAFE = "safe"
    CONFIRM = "confirm"
    DENY = "deny"


@dataclass
class UserRequest:
    text: str


@dataclass
class Intent:
    type: IntentType
    action: str
    target: str | None = None
    parameters: dict[str, Any] = field(default_factory=dict)
    confidence: float = 1.0


@dataclass
class PlanStep:
    id: str
    tool: str
    action: str
    parameters: dict[str, Any] = field(default_factory=dict)
    permission: PermissionLevel = PermissionLevel.SAFE


@dataclass
class Plan:
    steps: list[PlanStep] = field(default_factory=list)


@dataclass
class ExecutionResult:
    success: bool
    message: str
    data: Any = None
    error: str | None = None


@dataclass
class PermissionDecision:
    level: PermissionLevel
    reason: str
    approved: bool = False