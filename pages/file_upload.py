from playwright.sync_api import Page
import os


class FileUploadPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/upload"
        self.selectors = _Selectors()

    def visit(self):
        return self.page.goto(self.url)

    def verify_page_url(self):
        assert self.page.url == self.url, "Not on the File Upload page."

    def choose_file(self, fileName: str):
        return self.page.set_input_files(
            self.selectors.FILE_INPUT, f"{os.getcwd()}/data/files/{fileName}"
        )

    def click_upload_button(self):
        return self.page.locator(self.selectors.UPLOAD_BUTTON).click()

    def get_result_output(self):
        return self.page.locator(self.selectors.RESULT_OUTPUT)

    def get_error_message(self):
        return self.page.locator(self.selectors.ERROR_MESSAGE)


class _Selectors:
    FILE_INPUT = "#file-upload"
    UPLOAD_BUTTON = "#file-submit"
    RESULT_OUTPUT = "#uploaded-files"
    ERROR_MESSAGE = "h1"
