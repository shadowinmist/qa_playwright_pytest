import re
import os
from asyncio import wait
from time import sleep
import pytest
from playwright.sync_api import Page, expect
import pytest_playwright
from pytest_html.extras import url


# 5 najważniejszych Assertions
# 1. to_be_visible()
# python
# expect(page.get_by_text("Success")).to_be_visible()
# 2. to_have_url()
# python
# expect(page).to_have_url(re.compile("contact"))
# 3. to_have_title()
# python
# expect(page).to_have_title(re.compile("Contact"))
# 4. to_have_value()
# python
# expect(page.get_by_placeholder("Search")).to_have_value("ugabuga")
# 5. to_have_count()
# python
# expect(page.locator("img")).to_have_count(3)

@pytest.mark.playwright
def test_link_link(locators_page: Page):


   # expect(page).to_have_title(re.compile(".*expand.testing.*"))
    link = locators_page.get_by_role("link", name="Contact")
    link.click()
    send_btn = locators_page.get_by_role("Link", name="Send")
    expect(send_btn).to_be_visible()

@pytest.mark.playwright
def test_link_text(locators_page: Page):

  #  expect(page).to_have_title(re.compile("expandtesting"))
    link = locators_page.get_by_text("Contact")
    link.click()
    send_btn = locators_page.get_by_role("Link", name="Send")
    expect(send_btn).to_be_visible()
 #   expect(page).to_have_title(re.compile("contact"))

@pytest.mark.playwright
def test_visible_btn(locators_page: Page):
    btns = locators_page.get_by_role("button")
    visible_btn = btns.filter(visible=True)
    expect(btns).to_have_count(3)
    expect(visible_btn).to_have_count(3)

@pytest.mark.playwright
def test_or_buttons(locators_page: Page):
    reload = locators_page.get_by_role("button", name="Reload")
    submit = locators_page.get_by_role("button", name="Submit")

    either = reload.or_(submit)
    expect(either).to_have_count(1)

@pytest.mark.playwright
def test_and_locator(locators_page: Page):
    buttons = locators_page.get_by_role("button")
    reload_text = locators_page.get_by_text("Reload")

    combined = buttons.and_(reload_text)
    expect(combined).to_have_count(1)

@pytest.mark.playwright
def test_headings_without_get(locators_page: Page):
    headings = locators_page.get_by_role("heading")
    no_get = headings.filter(has_not_text="get")
    expect(no_get).to_have_count(6)

@pytest.mark.playwright
def test_placeholder(locators_page: Page):
  #  expect(page).to_have_title(re.compile("expandtesting"))
    placeholder = locators_page.get_by_placeholder("Search the site")
    placeholder.fill("ugabuga")
    placehold = locators_page.get_by_role("placeholder", name="Search the site")
    placehold.fill("ugabuga")
    placeholder = locators_page.get_by_placeholder("Filter by tag")
    placeholder.fill("ugabuga")
    sleep(4)
    expect(locators_page.get_by_placeholder("Search the site")).to_have_value("ugabuga")
    expect(locators_page.get_by_placeholder("Filter by tag")).to_have_value("ugabuga")


@pytest.mark.playwright
def test_alttext(locators_page: Page):
    locators_page.goto("https://practice.expandtesting.com/locators")
  #  expect(page).to_have_title(re.compile("expandtesting"))
    alttext = locators_page.get_by_alt_text("User avatar")
    alttext.click()
    expect(locators_page.get_by_alt_text("User avatar")).to_be_visible()

@pytest.mark.playwright
def test_snapshot(locators_page: Page):
  #  expect(page).to_have_title(re.compile("expandtesting"))
    alttext = locators_page.get_by_alt_text("User avatar")
    alttext.click()
    locators_page.screenshot(path="screenshot.png")
    expect(locators_page.get_by_alt_text("User avatar")).to_be_visible()

@pytest.mark.playwright
def test_img_count(locators_page: Page):
  #  expect(page).to_have_title(re.compile("expandtesting"))
    image = locators_page.locator("img")
    expect(locators_page).to_have_count(2)



@pytest.mark.playwright
def test_getbytitle(locators_page: Page):
  #  expect(page).to_have_title(re.compile("expandtesting"))
    title = locators_page.get_by_title("Refresh content")
    title.click()
    expect(title).to_be_visible()

    settings = locators_page.get_by_title("Settings")
    expect(settings).to_be_visible()


@pytest.mark.playwright
def test_chaining_placeholder(locators_page: Page):
    main = locators_page.locator("main")
    search_input = main.get_by_placeholder("Search the site")

    search_input.fill("playwright")
    expect(search_input).to_have_value("playwright")


@pytest.mark.playwright
def test_filter(locators_page: Page):

    #1
    section = locators_page.locator("main").filter(has_text="Locators")
    expect(section).to_be_visible()

    #2
    main = locators_page.get_by_role("main")
    section = locators_page.locator("Section").filter(has=locators_page.get_by_role("link",name="Contact"))


@pytest.mark.playwright
def test_first_link(locators_page: Page):
    links = locators_page.locator("a")
    first_link = links.first

    expect(first_link).to_be_visible()
    expect(first_link).to_have_text("Buy 1 Get 1 Free")

@pytest.mark.playwright
def test_last_link(page: Page):
    page.goto("https://practice.expandtesting.com/locators")

    links = page.locator("a")
    last_link = links.last

    expect(last_link).to_be_visible()
    expect(last_link).to_have_text("Settings")

@pytest.mark.playwright
def test_nth_task(page: Page):
    page.goto("https://practice.expandtesting.com/locators")

    tasks = page.locator("li")
    second_task = tasks.nth(1)

    expect(second_task).to_be_visible()
    expect(second_task).to_have_text("Task 2: Implement")

@pytest.mark.playwright
def test_expandtesting_locators(locators_page):

    locator = locators_page.get_by_role("link", name="Contact")
    locator.click()
    print(locators_page.url)
    expect(locators_page).to_have_url(re.compile(".*cont.*"))
    main = locators_page.locator("main")
    expect(main).to_be_visible()

@pytest.mark.playwright
@pytest.mark.parametrize('search_item, found_item, should_fail', [
        ("Tips","tips", False),
        ("About","about", False),
        ("Contact","contact", False)])
def test_search_items_param(locators_page, search_item, found_item, should_fail):
    search =  locators_page.get_by_role("link",name=search_item)
    #print(locators_page.locator("body").aria_snapshot())
    search.click()
    if should_fail:
        with pytest.raises(AssertionError):
            expect(locators_page).to_have_url(re.compile(f".*{found_item}"))
    else:
        expect(locators_page).to_have_url(re.compile(f".*{found_item}"))
    #print(locators_page.url)

@pytest.mark.playwright
def test_filter_contacts(locators_page: Page):
    links = locators_page.get_by_role("link")
    contacts = links.filter(has_text="Contact")
    expect(contacts).to_have_count(1)
    expect(contacts).to_have_attribute("href", "/contact")

@pytest.mark.playwright
def test_table_row(locators_page: Page):
    row = locators_page.get_by_role("row").filter(has_text="Keyboard")
    cells = row.get_by_role("cell")
    expect(cells.nth(0)).to_have_text("Keyboard")
    expect(cells.nth(1)).to_have_text("Available")
    expect(cells.nth(2)).to_have_text("5")

@pytest.mark.playwright
def test_table_header(locators_page: Page):
    table = locators_page.get_by_role("table")
    header = table.get_by_role("columnheader")
    expect(header).to_have_count(3)
    expect(header).to_contain_text(["Product", "Status", "Stock"])

@pytest.mark.playwright
@pytest.mark.parametrize('heading_name, position',[
        ('🎯 getByRole', 1),
        ('📝 getByText', 2),
        ('🏷️ getByLabel',3),
        ('🔤 getByPlaceholder', 4),
        ('🖼️ getByAltText', 5),
        ('🏷️ getByTitle', 6),
        ('🧪 getByTestId', 7),
        ('🧭 Legacy CSS', 8)
])
def test_headers(locators_page: Page, heading_name, position):
    headings = locators_page.get_by_role("heading")
    expect(headings.nth(position)).to_have_text(heading_name)

@pytest.mark.playwright
def test_headers_with_get(locators_page: Page):
    headings = locators_page.get_by_role("heading")
    expect(headings).to_have_count(13)
    headings_with_get = headings.filter(has_text=re.compile(r"get"))
    expect(headings_with_get).to_have_count(7)

@pytest.mark.playwright
def test_hover_color(locators_page: Page):
    btn = locators_page.get_by_role("button").filter(has_text=re.compile(r"Add"))
    expect(btn).to_have_css("color", "rgb(255, 255, 255)")
    btn.hover()
    expect(btn).to_have_css("color", "rgb(255, 255, 255)")

@pytest.mark.playwright
def test_heading_after_click(locators_page: Page):
    Demos = locators_page.get_by_role("button", name="Demos")
    expect(locators_page.get_by_role("link", name="Examples")).not_to_be_visible()
    Demos.click()
    expect(locators_page.get_by_role("link", name="Examples")).to_be_visible()