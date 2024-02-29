from playwright.sync_api import Page
from pages.home import HomePage



def test_load_home_page(page: Page) -> None:
    # Initialize HomePage object
    homePage = HomePage(page)

    # Load Home Page
    homePage.visit()

    # Assert that the page title is correct
    assert page.title() == 'The Internet'
