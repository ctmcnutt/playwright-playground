from playwright.sync_api import Page

class FormAuthPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/login"
        self.selectors = _Selectors()

    def visit(self):
        return self.page.goto(self.url)

    def verify_page_url(self):
        assert self.page.url == self.url, "Not on the Form Authentication page."

    def login(self, username: str, password: str):
        self.page.fill(self.selectors.USERNAME_INPUT, username)
        self.page.fill(self.selectors.PASSWORD_INPUT, password)
        self.page.click(self.selectors.SUBMIT_BUTTON)

    def get_status_banner(self):
        return self.page.locator(self.selectors.STATUS_BANNER)

class _Selectors: 
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SUBMIT_BUTTON = "button[type='submit']"
    STATUS_BANNER = "#flash"