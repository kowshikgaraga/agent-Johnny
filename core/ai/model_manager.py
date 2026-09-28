from .engine import AIEngine


class ModelManager:

    def __init__(self, default_engine: AIEngine):
        self.default_engine = default_engine

    def get_engine(self, task: str | None = None) -> AIEngine:
        """
        Return an AI engine appropriate for the task.

        v1 always returns the default engine.
        """
        return self.default_engine