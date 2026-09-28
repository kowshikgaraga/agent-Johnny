import platform


class SystemTool:

    def info(self) -> dict[str, str]:
        return {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        }