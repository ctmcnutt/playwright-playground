from playwright.sync_api import Page

class FormAuthPage:
    def __init__(self, page: Page):
        self.selectors = _Selectors()
        self.page = page

    def visit(self):
        return self.page.goto("https://the-internet.herokuapp.com/login")

    def verify_page_url(self):
        assert self.page.url() == self.url, "Not on the Form Authentication page."

    def login(self, username: str, password: str):
        self.page.fill(self.selectors.USERNAME_INPUT, username)
        self.page.fill(self.selectors.PASSWORD_INPUT, password)
        self.page.click(self.selectors.SUBMIT_BUTTON)

    def get_status_banner(self):
        return self.page.locator()

class _Selectors: 
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SUBMIT_BUTTON = "button[type='submit']"
    STATUS_BANNER = "#flash"