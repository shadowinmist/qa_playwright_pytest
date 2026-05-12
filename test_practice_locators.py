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

