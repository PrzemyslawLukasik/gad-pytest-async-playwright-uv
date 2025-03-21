import pytest


@pytest.mark.with_ids
@pytest.mark.asyncio(loop_scope="session")
async def test_label_txt(without_ids_actions) -> None:
    # Visit Simple Elements page with ids
    await without_ids_actions.visit()

    # Get the label element text
    text = await without_ids_actions.get_label_txt()
    # Assert text equals: Some text for label
    assert (
        "Some text for label" == text
    ), f"Label text not match Label: '{text}'"


@pytest.mark.with_ids
@pytest.mark.asyncio(loop_scope="session")
async def test_push_button(without_ids_actions) -> None:
    # Visit Simple Element page with ids
    await without_ids_actions.visit()

    # Click the button and verify the result
    await without_ids_actions.click_on_click_me_btn()


@pytest.mark.with_ids
@pytest.mark.asyncio(loop_scope="session")
async def test_select_checkbox(without_ids_actions) -> None:
    # Visit Simple Elements page with ids
    await without_ids_actions.visit()

    # Select checkbox
    await without_ids_actions.select_checkbox()

    # Deselect checkbox
    await without_ids_actions.deselect_checkbox()


@pytest.mark.with_ids
@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.parametrize("button_no", [1, 2, 3])
async def test_radio_buttons(without_ids_actions, button_no) -> None:
    # Visit Simple Element page with ids
    await without_ids_actions.visit()

    # Click on radio button an verify it's clicked
    await without_ids_actions.check_radio_no(button_no)


@pytest.mark.with_ids
@pytest.mark.asyncio(loop_scope="session")
async def test_input_field(without_ids_actions) -> None:
    # Visit Simple Element page with ids
    await without_ids_actions.visit()

    # Fill in the input field with "test" and verify the result
    await without_ids_actions.fill_in_input_value("test")


@pytest.mark.with_ids
@pytest.mark.asyncio(loop_scope="session")
async def test_text_area(without_ids_actions) -> None:
    # Visit Simple Element page with ids
    await without_ids_actions.visit()

    # Fill in the text area and verify the result field fill_in_input_value
    await without_ids_actions.fill_in_text_area("Test\nTest2")


@pytest.mark.with_ids
@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.parametrize("option_value", ["option1", "option2", "option3"])
async def test_select_option_in_dropdown(
    without_ids_actions, option_value
) -> None:
    # Visit Simple Element page with ids
    await without_ids_actions.visit()

    # select option: option2 and verify result field value
    await without_ids_actions.select_dd_option(option_value)


@pytest.mark.with_ids
@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.parametrize("slider_value", [1, 100, 55])
async def test_slider_item(without_ids_actions, slider_value) -> None:
    # Visit Simple Elements page with ids
    await without_ids_actions.visit()

    # Set a slider value and verify the result
    await without_ids_actions.set_slider_value(slider_value)


@pytest.mark.with_ids
@pytest.mark.asyncio(loop_scope="session")
async def test_hover_over_label(without_ids_actions) -> None:
    # Visit Simple Elements page with ids
    await without_ids_actions.visit()

    # Hover over label and verify results
    await without_ids_actions.hover_over_hover_label()


@pytest.mark.with_ids
@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.parametrize(
    "test_date", ["1900-01-01", "2024-06-15", "2300-12-31"]
)
async def test_date_change(without_ids_actions, test_date) -> None:
    # Visit Simple Elements with ids page
    await without_ids_actions.visit()

    # Set date and verify the result
    await without_ids_actions.set_date(test_date)


@pytest.mark.with_ids
@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.parametrize("hex_color", ["#000000", "#ffffff", "#7f3b22"])
async def test_select_color(without_ids_actions, hex_color) -> None:
    # Visit Simple Elements with ids page
    await without_ids_actions.visit()

    # Select colot and verify the result
    await without_ids_actions.select_color_by_hex(hex_color)
