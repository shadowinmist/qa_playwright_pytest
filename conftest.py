import pytest
from datetime import datetime
import os

from playwright.async_api import Page
from pygments.styles.dracula import yellow


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = f"reports/playwright_report_{timestamp}.html"
    config.option.htmlpath = report_path
    print(f"Raport zapisany jako: {report_path}")



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
            page.screenshot(path=f"screenshots/{item.name}.png")