import pytest
from playwright.sync_api import Page

def test_sample(page:Page):
    page.goto("https://www.google.com")

    try:
        page.get_by_role("button", name="Zaakceptuj wszystko").click()
    except:
        print("nothing to click")
    finally:
        page.get_by_role("combobox", name="Szukaj").fill("uuuaaa")
        page.keyboard.press("Enter")
