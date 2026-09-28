from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Config:
    ollama_url: str = "http://localhost:11434"
    default_model: str = "llama3.2"
    max_plan_steps: int = 10
    require_confirmation: bool = True

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            ollama_url=os.getenv(
                "OLLAMA_URL",
                "http://localhost:11434",
            ),
            default_model=os.getenv(
                "AI_MODEL",
                "llama3.2",
            ),
            max_plan_steps=int(
                os.getenv("MAX_PLAN_STEPS", "10")
            ),
            require_confirmation=os.getenv(
                "REQUIRE_CONFIRMATION",
                "true",
            ).lower() == "true",
        )