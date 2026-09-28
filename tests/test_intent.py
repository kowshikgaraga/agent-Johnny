from core.intent import IntentDetector
from core.types import IntentType, UserRequest


def test_open_app_intent():

    detector = IntentDetector()

    intent = detector.detect(
        UserRequest("Open Chrome")
    )

    assert intent.type == IntentType.APP_OPERATION
    assert intent.action == "open"
    assert intent.target == "Chrome"


def test_question_intent():

    detector = IntentDetector()

    intent = detector.detect(
        UserRequest("What is Python?")
    )

    assert intent.type == IntentType.QUESTION