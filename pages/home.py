from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.url = "https://the-internet.herokuapp.com/"

    def visit(self):
        self.page.goto(self.url)
