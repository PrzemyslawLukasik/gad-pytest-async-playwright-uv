from playwright.async_api import Page


class BasePage:
    """
    Base Page class
    """

    def __init__(self, page: Page):
        self.page = page
        self.url = "/"

    async def _visit(self, url: str) -> None:
        await self.page.goto(self.url)