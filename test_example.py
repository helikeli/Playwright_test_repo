import pytest
from playwright.sync_api import Page, expect, Playwright



def test_search(page : Page, playwright: Playwright):
    playwright.selectors.set_test_id_attribute("testid")

    page.goto("https://www.seznam.cz")
    page.get_by_test_id("button-agree").click()
    expect(page.get_by_text("Mapy")).to_be_visible()

def test_wrong_title(page : Page):
    '''
        Test that the correct title is displayed on CPME GUI.
    '''
    page.goto("https://www.seznam.cz")
    assert page.title() == "Seznam najdu tam, co neznam"

