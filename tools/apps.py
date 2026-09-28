class AppTool:

    def open(self, app: str) -> str:
        # Real OS implementation can be added later.
        return f"Requested opening application: {app}"

    def close(self, app: str) -> str:
        return f"Requested closing application: {app}"