import pytest
from playwright.sync_api import Playwright


# chrome setup fixture
@pytest.fixture(scope='function')
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
