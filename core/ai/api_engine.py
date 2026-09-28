import requests

from .engine import AIEngine


class APIEngine(AIEngine):

    def __init__(
        self,
        base_url: str,
        api_key: str,
        model: str,
        timeout: int = 120,
    ):
        self.base_url = base_url
        self.api_key = api_key
        self.model = model
        self.timeout = timeout
        self.headers = {
            "Content-Type": "application/json",
        }
        if self.api_key:
            self.headers["Authorization"] = f"Bearer {self.api_key}"

    def __repr__(self) -> str:
        return (
            f"APIEngine(base_url={self.base_url!r}, "
            f"model={self.model!r}, timeout={self.timeout})"
        )

    def __str__(self) -> str:
        return self.__repr__()

    def generate(self, prompt: str) -> str:
        headers = dict(self.headers)
        if self.api_key and "Authorization" not in headers:
            headers["Authorization"] = f"Bearer {self.api_key}"

        payload = {
            "model": self.model,
            "prompt": prompt,
        }

        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()
        except requests.RequestException as exc:
            if self.api_key and self.api_key in str(exc):
                sanitized_msg = str(exc).replace(self.api_key, "[REDACTED]")
                try:
                    new_exc = type(exc)(sanitized_msg)
                except Exception:
                    new_exc = requests.RequestException(sanitized_msg)
                raise new_exc from None
            raise

        try:
            data = response.json()
        except ValueError:
            return response.text

        if isinstance(data, dict):
            if "choices" in data and isinstance(data["choices"], list) and data["choices"]:
                first_choice = data["choices"][0]
                if isinstance(first_choice, dict):
                    message = first_choice.get("message")
                    if isinstance(message, dict) and "content" in message and message["content"] is not None:
                        return str(message["content"])
                    if "text" in first_choice and first_choice["text"] is not None:
                        return str(first_choice["text"])

            for key in ("text", "response", "generated_text", "content", "output", "result"):
                if key in data and data[key] is not None:
                    return str(data[key])

            return str(data)

        if isinstance(data, str):
            return data

        return response.text