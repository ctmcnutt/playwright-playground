from playwright.sync_api import Page

class AddRemoveElementsPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/add_remove_elements/"
        self.selectors = _Selectors()

    def visit(self):
        self.page.goto(self.url)

    def get_add_button(self):
        return self.page.locator(self.selectors.ADD_BUTTON)

    def get_delete_button(self):
        return self.page.locator(self.selectors.DELETE_BUTTON)

    def get_added_elements_count(self):
        return len(self.get_delete_button)

    def verify_page_url(self):
        assert self.page.url() == self.url, "Not on the Add/Remove Elements page."

class _Selectors: 
    ADD_BUTTON = "#content > .example > button"
    DELETE_BUTTON = "#elements > button"
