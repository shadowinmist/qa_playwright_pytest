import re
import os
import pytest
from playwright.sync_api import Page, expect
import pytest_playwright


@pytest.mark.regression
@pytest.mark.playwright
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


@pytest.mark.regression
@pytest.mark.parametrize('link_name', [
    "Get started",
    "Docs",
    "API",
    "Community"
])

def test_top_nav_links(page: Page, link_name, ):

    page.goto("https://playwright.dev/")
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))



    page.get_by_role("link",name= link_name).click()
    page.wait_for_url("https://playwright.dev/docs/intro")

    expect(page).to_have_title(re.compile("Playwright"))



def test_okienko(playwright_page):
    # 1. KROK PIERWSZY: Klikamy w przycisk otwierający wyszukiwarkę.
    # Używamy get_by_role, ponieważ jak wspominałem, "Search" na górze to przycisk, a nie pole tekstowe.
    playwright_page.get_by_role("button", name="Search").click()

    # 2. KROK DRUGI: Teraz otwiera się okienko. Szukamy w nim PRAWDZIWEGO pola wejściowego.
    # W nowym okienku pole input ma placeholder "Search docs".
    # szukajka = playwright_page.get_by_placeholder("Search")
    playwright_page.keyboard.press("Control+K")
    szukajka = playwright_page.get_by_placeholder("Search docs")

    # 3. Wpisujemy tekst i zatwierdzamy
    szukajka.fill("css")
    szukajka.press("Enter")
    print(playwright_page.url)
    # 4. Sprawdzamy czy adres strony zawiera słowo "css"
    expect(playwright_page).to_have_url(re.compile('css'))

@pytest.mark.regression
def test_get_by_role_github(playwright_page):
    with playwright_page.expect_popup() as popup_info:
        playwright_page.get_by_role("link", name="GitHub repository").click()
    new_tab = popup_info.value
    #expect(new_tab).to_be_visible()
    expect(new_tab).to_have_url(re.compile(".*/git.*"))

@pytest.mark.regression
def test_print_aria_tree(playwright_page):
    snapshot = playwright_page.locator("body").aria_snapshot()
    print(snapshot)

@pytest.mark.regression
def test_get_by_text_git(page):
    page.goto("https://playwright.dev/")
    with page.expect_popup() as popup_info:
        page.get_by_text("Star", exact=True).click()

    new_tab = popup_info.value
    expect(new_tab).to_have_url(re.compile(".*github.*"))


@pytest.mark.regression
def test_example(page):
    page.goto("https://playwright.dev/")

    label = page.get_by_label("Email")
    print(label.count())
    assert label.count() == 0

    labels = page.locator("button")
    print(labels.count())
    assert labels.count() > 0


def test_search_docs(page: Page):
    page.goto("https://google.pl")
    page.get_by_placeholder("Szukaj").click()
    page.get_by_placeholder("Szukaj").fill("locators")
    page.get_by_placeholder("Szukaj").press("Enter")
    expect(page).to_have_url(re.compile("locators"))


@pytest.mark.regression
@pytest.mark.parametrize('search_item, found_item, should_fail', [
        ("Tips","tips", False),
        ("About","about", False),
        ("Contact","contact", False)])
def test_serach_items_param(locators_page, search_item, found_item, should_fail):
    search =  locators_page.get_by_role("link",name=search_item)
    print(locators_page.locator("body").aria_snapshot())
    search.click()
    if should_fail:
        with pytest.raises(AssertionError):
            expect(locators_page).to_have_url(re.compile(f".*{found_item}"))
    else:
        expect(locators_page).to_have_url(re.compile(f".*{found_item}"))
    print(locators_page.url)
