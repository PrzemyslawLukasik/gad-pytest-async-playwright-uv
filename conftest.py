import pytest
import pytest_playwright_asyncio

from pathlib import Path

from src.helpers.screenshots import Screenshots


def pytest_addoption(parser):
    """Custom input parameters
    """

    parser.addoption(
        "--baseurl",
        action="store",
        dest="base_url",
        default="http://localhost:3000",
        help="Application Under Tests url"
    )
    parser.addoption(
        "--screenshots-path",
        action="store",
        dest="screenshots_path",
        default="artefacts/screenshots",
        help="Screenshots path"
    )
    parser.addoption(
        "--additional-info",
        action="store",
        dest="additional_info",
        default="Build: ",
        help="Additional build notation"
    )


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    pytest.env = {}
    pytest.env["base_url"] = config.option.base_url
    pytest.env["additional_info"] = config.option.additional_info
    return pytest.env