from dataclasses import dataclass
from playwright.async_api import Page, Locator, expect


@dataclass
class MainPageLocators:
    page: Page

    def lets_start_btn_locator(self) -> Locator:
        return self.page.get_by_role("button", name="Let's start!")

    def practice_pages_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Practice pages")


class MainPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = MainPageLocators(self.page)
        self.url = "http://localhost:3000"

    async def visit(self) -> None:
        await self.page.goto(self.url)

    async def click_on_practice_pages_btn(self) -> None:
        await self.locators.practice_pages_btn().click()
