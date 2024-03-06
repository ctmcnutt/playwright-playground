from pages.form_auth import FormAuthPage
from pages.secure import SecurePage
from dotenv import load_dotenv
import os

load_dotenv()

# Test Case:
# Given on the Form Authentication page
# When submitting valid credentials
# Then successfully logged in to secure page

def test_form_authentication_successful_login(page):
    form_auth_page = FormAuthPage(page)
    secure_page = SecurePage(page)

    # Given on the Form Authentication page
    form_auth_page.visit()

    # When submitting valid credentials
    form_auth_page.login(os.getenv("FORM_AUTHENTICATION_USERNAME"), os.getenv("FORM_AUTHENTICATION_PASSWORD"))

    # Then successfully logged in to secure page
    assert "success" in secure_page.get_status_banner().get_attribute('class')