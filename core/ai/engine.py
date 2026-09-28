from abc import ABC, abstractmethod


class AIEngine(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from a prompt."""
        raise NotImplementedError