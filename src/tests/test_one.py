import logging

import pytest
from playwright.async_api import Page

from src.pages.main_page import MainPage
from src.pages.practice_page import PracticePage

my_logger = logging.getLogger(__name__)


@pytest.mark.one
@pytest.mark.asyncio(loop_scope="session")
async def test_open_practice_page(page: Page) -> None:
    main_page = MainPage(page)
    practice_page = PracticePage(page)
    await main_page.visit()
    await main_page.click_on_practice_pages_btn()
    await practice_page.is_practice_page_open()

    my_logger.warning("WARNING")
    my_logger.info(f"pytest.env: {pytest.env}")
