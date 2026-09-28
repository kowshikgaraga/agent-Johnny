from .types import (
    Intent,
    IntentType,
    UserRequest,
)


class IntentDetector:

    def detect(self, request: UserRequest) -> Intent:
        text = request.text.strip()
        lower = text.lower()

        if lower.startswith(("hi", "hello", "hey")):
            return Intent(
                type=IntentType.CHAT,
                action="chat",
            )

        if "open " in lower:
            target = text[lower.index("open ") + 5:].strip()

            return Intent(
                type=IntentType.APP_OPERATION,
                action="open",
                target=target,
            )

        if any(
            word in lower
            for word in ["find file", "search files", "find my file"]
        ):
            return Intent(
                type=IntentType.FILE_OPERATION,
                action="search",
                parameters={"query": text},
            )

        if lower.startswith(("what ", "who ", "why ", "how ")):
            return Intent(
                type=IntentType.QUESTION,
                action="answer",
            )

        return Intent(
            type=IntentType.UNKNOWN,
            action="unknown",
            confidence=0.2,
        )