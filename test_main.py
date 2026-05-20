import re
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.playwright
def test_get_started_link(playwright_page: Page):

    get_started = playwright_page.get_by_role("link", name="Get started")
    get_started.click()
    expect(get_started).to_have_attribute("href", "/docs/intro")
    expect(playwright_page.get_by_role("heading", name="Installation")).to_be_visible()

@pytest.mark.regression
@pytest.mark.playwright
def test_get_seatch_btn(playwright_page: Page):

    get_btn = playwright_page.get_by_role("button", name="Search")
    search_input = get_btn.get_by_placeholder("Search docs")
    expect(get_btn).to_be_visible()
    expect(search_input).to_be_hidden()
    get_btn.click()
    expect(search_input).to_be_visible()

@pytest.mark.regression
@pytest.mark.playwright
def test_search_input(playwright_page: Page):
    playwright_page.get_by_role("button", name="Search").click()
    search_input = playwright_page.get_by_placeholder("Search docs")
    search_input.fill("css")
    expect(search_input).to_have_value("css")

@pytest.mark.regression
def test_search_modal_or(playwright_page: Page):
    playwright_page.get_by_role("button", name="Search").click()
    search_input = playwright_page.get_by_placeholder("Search docs")
    heading = playwright_page.get_by_role("heading", name="Search")
    combined = search_input.or_(heading)
    expect(combined.first).to_be_visible()

@pytest.mark.regression
@pytest.mark.parametrize(
    "link_name, expected_url",
    [
        ("Get started", r".*/docs/intro"),
        ("Docs", r".*/docs/intro"),
        ("API", r".*/docs/api/.*"),
    ],
)
def test_top_nav_links(playwright_page: Page, link_name, expected_url):
    playwright_page.get_by_role("link", name=link_name).click()
    expect(playwright_page).to_have_url(re.compile(expected_url))


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

def test_print_aria_tree(playwright_page):
    snapshot = playwright_page.locator("body").aria_snapshot()
    print(snapshot)

@pytest.mark.regression
def test_get_by_text_git(playwright_page):
    playwright_page.goto("https://playwright.dev/")
    with playwright_page.expect_popup() as popup_info:
        playwright_page.get_by_text("Star", exact=True).click()

    new_tab = popup_info.value
    expect(new_tab).to_have_url(re.compile(".*github.*"))


@pytest.mark.regression
def test_example(playwright_page: Page):
    playwright_page.goto("https://playwright.dev/")

    label = playwright_page.get_by_label("Email")
    print(label.count())
    assert label.count() == 0

    labels = playwright_page.locator("button")
    print(labels.count())
    assert labels.count() > 0


def test_search_docs(page: Page):
    page.goto("https://google.pl")
    page.get_by_placeholder("Szukaj").click()
    page.get_by_placeholder("Szukaj").fill("locators")
    page.get_by_placeholder("Szukaj").press("Enter")
    expect(page).to_have_url(re.compile("locators"))



@pytest.mark.regression

def test_get_github_page(playwright_page: Page):
    with playwright_page.expect_popup() as popup_info:
        github_link = playwright_page.get_by_role("link", name="GitHub repository")
        github_link.click()
    new_tab = popup_info.value
    expect(new_tab).to_have_url(re.compile(".*github.*"))
    expect(new_tab).to_have_title(re.compile("GitHub"))
