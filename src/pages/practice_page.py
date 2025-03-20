from dataclasses import dataclass

from playwright.async_api import Locator, Page, expect


@dataclass
class PracticePageLocators:
    page: Page

    def practice_page_title(self) -> Locator:
        return self.page.get_by_role(
            "heading", name="Practice your test automation"
        )

    def with_ids_btn(self) -> Locator:
        return self.page.get_by_role("button", name="With IDs")


class PracticePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = PracticePageLocators(self.page)

    async def is_practice_page_open(self) -> bool:
        return not await expect(
            self.locators.practice_page_title()
        ).to_be_visible()

    async def click_on_with_ids_btn(self) -> None:
        await self.locators.with_ids_btn().click()
