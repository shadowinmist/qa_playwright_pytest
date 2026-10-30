import re
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.playwright
def test_link_link(helion_page: Page):
    # facebook_by_role = helion_page.get_by_role("link", name="Facebook")
    # expect(facebook_by_role).to_be_visible()

    links = helion_page.locator("a")
    print(links, links.count())

def test_znajdz_sociale(page: Page):
    page.goto("https://helion.pl", wait_until="domcontentloaded")

    # Pozwól stronie dokończyć renderowanie dynamicznych elementów.
    page.wait_for_timeout(2_000)

    links = page.locator("a")

    print(f"\nWszystkich <a> na stronie: {links.count()}\n")

    for i in range(links.count()):
        link = links.nth(i)

        href = link.get_attribute("href") or ""
        title = link.get_attribute("title") or ""
        aria_label = link.get_attribute("aria-label") or ""

        # Szukamy danych wskazujących na Facebooka.
        if "facebook" in f"{href} {title} {aria_label}".lower():
            print(f"INDEX: {i}")
            print(f"href: {href}")
            print(f"title: {title}")
            print(f"aria-label: {aria_label}")
            print("HTML:")
            print(link.evaluate("(el) => el.outerHTML"))
            print("-" * 70)
    page.click(href)
def test_inspekcja_footer(page: Page):
    """Inspekcja wszystkich linków w footerze"""

    page.goto("https://helion.pl", wait_until="networkidle")

    # Znajdź footer
    footer = page.locator("footer")

    # Sprawdź, czy footer istnieje
    if footer.count() > 0:
        print("✓ Footer znaleziony")

        # Wszystkie linki w footerze
        links = footer.locator("a")
        count = links.count()
        print(f"Liczba linków w footerze: {count}")

        # Iteracja po linkach
        for i in range(count):
            link = links.nth(i)
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"[{i}] {text} -> {href}")

            # Sprawdź, czy to Facebook
            if "facebook" in (href or "").lower():
                print(f"🎯 ZNALEZIONO FACEBOOK: {href}")


def test_inspector(page: Page):
    page.goto("https://helion.pl")

    # Przewiń stronę na dół, aby ikony z lewej były w widocznym obszarze.
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # Test zatrzyma się tutaj.
    page.pause()