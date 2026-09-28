class BrowserTool:

    def open_url(self, url: str) -> str:
        return f"Requested opening URL: {url}"

    def search(self, query: str) -> str:
        return f"Requested browser search: {query}"