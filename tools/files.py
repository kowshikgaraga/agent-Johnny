from pathlib import Path


class FileTool:

    def search(self, query: str) -> list[str]:
        root = Path.home()

        matches = []

        for path in root.rglob("*"):
            if path.is_file() and query.lower() in path.name.lower():
                matches.append(str(path))

        return matches[:50]

    def read(self, path: str) -> str:
        return Path(path).read_text(
            encoding="utf-8"
        )