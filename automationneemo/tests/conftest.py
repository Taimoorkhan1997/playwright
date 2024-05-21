import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright


@pytest.fixture()
def set_up_tear_down(page) -> None:
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://www.saucedemo.com")
    yield page


