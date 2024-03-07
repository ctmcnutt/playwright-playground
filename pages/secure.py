from playwright.sync_api import Page


class SecurePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/secure"
        self.selectors = _Selectors()

    def visit(self):
        self.page.goto(self.url)

    def verify_page_url(self):
        assert self.page.url == self.url, "Not on the Secure Logged In page."

    def logout(self):
        self.page.click(self.selectors.LOGOUT_BUTTON)

    def get_status_banner(self):
        return self.page.locator(self.selectors.STATUS_BANNER)


class _Selectors:
    LOGOUT_BUTTON = "a.button[href='/logout']"
    STATUS_BANNER = "#flash"
