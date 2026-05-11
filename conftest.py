import pytest
from datetime import datetime
import os
from playwright.sync_api import Page

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)

    # timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # report_path = f"reports/playwright_report_{timestamp}.html"
    # config.option.htmlpath = report_path
    # print(f"Raport zapisany jako: {report_path}")

@pytest.fixture
def locators_page(page: Page):
    page.goto("https://practice.expandtesting.com/locators")
    yield page

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)
