from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def visit(self):
        self.page.goto('https://the-internet.herokuapp.com/')

