import re

from playwright.async_api import Page, expect

from src.pages.base_page import BasePage


class SimpleElementsActions(BasePage):
    """
    Simple elements page
    """

    def __init__(self, page: Page, locators):
        super().__init__(page)
        self.locators = locators

        self.url = locators.url

    async def visit(self) -> None:
        """
        Open page
        """
        await self._visit(self.url)
        await expect(self.locators.results_container()).to_be_visible()

    async def get_label_txt(self) -> str:
        """
        Get The label text
        """
        return await self.locators.label().inner_text()

    async def click_on_click_me_btn(self) -> None:
        await self.locators.click_me_btn().click()
        await expect(self.locators.result_value()).to_have_text(
            "You clicked the button!"
        )

    async def is_checkbox_selected(self) -> bool:
        return (
            True if await self.locators.checkbox_input().is_checked() else False
        )

    async def select_checkbox(self) -> None:
        if not await self.is_checkbox_selected():
            await self.locators.checkbox_input().click()
            await expect(self.locators.result_value()).to_have_text(
                "Checkbox is checked!"
            )

    async def deselect_checkbox(self) -> None:
        if await self.is_checkbox_selected():
            await self.locators.checkbox_input().click()
            await self.locators.checkbox_input().scroll_into_view_if_needed()
            await expect(self.locators.result_value()).to_have_text(
                "Checkbox is unchecked!"
            )

    async def check_radio_no(self, no: int) -> None:
        await self.locators.__getattribute__(f"radio_btn_{no}")().click()
        await expect(self.locators.result_value()).to_have_text(
            f"Radio Button {no} clicked!"
        )

    async def check_radio_btn_1(self) -> None:
        await self.check_radio_no(1)

    async def check_radio_btn_2(self) -> None:
        await self.check_radio_no(2)

    async def check_radio_btn_3(self) -> None:
        await self.check_radio_no(3)

    async def fill_in_input_value(self, text: str) -> None:
        await self.locators.input_field().fill(text)
        await self.locators.input_field().press("Enter")
        await self.locators.result_value().scroll_into_view_if_needed()
        await expect(self.locators.result_value()).to_have_text(
            "Input value changed to: " + text
        )

    async def fill_in_text_area(self, text: str) -> None:
        await self.locators.text_area().fill(text)
        await self.locators.text_area().press("Tab")
        await expect(self.locators.result_value()).to_have_text(
            "Textarea value changed to: " + text
        )

    async def select_dd_option(self, option: str) -> None:
        await self.locators.droprown_menu().click()
        await self.locators.droprown_menu().select_option(value=option)
        await self.locators.droprown_menu().scroll_into_view_if_needed()
        await expect(self.locators.result_value()).to_have_text(
            "Selected option: " + option
        )

    async def set_slider_value(self, value: int) -> None:
        await self.locators.slider().fill(str(value))
        await self.locators.result_value().scroll_into_view_if_needed()
        await expect(self.locators.result_value()).to_have_text(
            "Range value changed to: " + str(value)
        )

    async def hover_over_hover_label(self) -> None:
        await self.locators.results_container().scroll_into_view_if_needed()
        await self.locators.hover_label().hover()
        await expect(self.locators.result_value()).to_have_text(
            "Mouse over event occurred!"
        )

    async def set_date(self, date: str) -> None:
        """
        Date has to be a string in format: yyyy-mm-dd
        """
        await self.locators.results_container().scroll_into_view_if_needed()
        await self.locators.date_field().fill(date)
        await self.locators.date_field().press("Tab")
        await expect(self.locators.result_value()).to_have_text(
            "Selected date: " + date
        )

    async def select_color_by_hex(self, hex_color: str) -> None:
        """
        Provide color in hex triplet: #7a223b
        """
        await self.locators.results_container().scroll_into_view_if_needed()
        await self.locators.color_pick().fill(hex_color)
        hex_color = hex_color.lstrip("#")
        splitted = re.findall(r".{1,2}", hex_color)
        dec_color = [int(color, 16) for color in splitted]
        await expect(self.locators.result_value()).to_have_text(
            f"New selected color: #{hex_color} as hex and in RGB: rgb{tuple(dec_color)}"
        )
