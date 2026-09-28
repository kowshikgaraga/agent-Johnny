import os

from .engine import AIEngine


class LocalEngine(AIEngine):

    def __init__(
        self,
        model_path: str,
        n_ctx: int = 4096,
        n_threads: int | None = None,
        n_gpu_layers: int = 0,
    ):
        self.model_path = model_path
        self.n_ctx = n_ctx
        self.n_threads = n_threads
        self.n_gpu_layers = n_gpu_layers
        self._llm = None

    def __repr__(self) -> str:
        return (
            f"LocalEngine(model_path={self.model_path!r}, "
            f"n_ctx={self.n_ctx}, n_threads={self.n_threads}, "
            f"n_gpu_layers={self.n_gpu_layers})"
        )

    def __str__(self) -> str:
        return self.__repr__()

    def generate(self, prompt: str) -> str:
        if self._llm is None:
            if not self.model_path or not os.path.exists(self.model_path):
                raise FileNotFoundError(
                    f"Model file does not exist: {self.model_path}"
                )

            try:
                from llama_cpp import Llama
            except ImportError as exc:
                raise ImportError(
                    "llama-cpp-python is not installed. Please install it with 'pip install llama-cpp-python'."
                ) from exc

            kwargs = {
                "model_path": str(self.model_path),
                "n_ctx": self.n_ctx,
                "n_gpu_layers": self.n_gpu_layers,
            }
            if self.n_threads is not None:
                kwargs["n_threads"] = self.n_threads

            self._llm = Llama(**kwargs)

        response = self._llm(prompt)

        if isinstance(response, dict):
            if "choices" in response and isinstance(response["choices"], list) and response["choices"]:
                first_choice = response["choices"][0]
                if isinstance(first_choice, dict):
                    if "text" in first_choice and first_choice["text"] is not None:
                        return str(first_choice["text"])
                    if "message" in first_choice and isinstance(first_choice["message"], dict):
                        return str(first_choice["message"].get("content", ""))
            for key in ("text", "response", "content"):
                if key in response and response[key] is not None:
                    return str(response[key])
            return str(response)

        if isinstance(response, str):
            return response

        return str(response)