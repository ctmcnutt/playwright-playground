from pages.form_auth import FormAuthPage
from pages.secure import SecurePage
from dotenv import load_dotenv
import os
from playwright.sync_api import Page

# Get the username/password combo from environment variables
load_dotenv()
valid_username = os.getenv("FORM_AUTHENTICATION_USERNAME")
valid_password = os.getenv("FORM_AUTHENTICATION_PASSWORD")

# Test Case:
# Given on the Form Authentication page
# When submitting valid credentials
# Then successfully logged in to secure page
# And able to successfully log out

def test_form_authentication_successful_login_logout(page: Page):
    form_auth_page = FormAuthPage(page)
    secure_page = SecurePage(page)

    # Given on the Form Authentication page
    form_auth_page.visit()

    # When submitting valid credentials
    form_auth_page.login(valid_username, valid_password)

    # Then successfully logged in to secure page
    secure_page.verify_page_url()
    assert "success" in secure_page.get_status_banner().get_attribute('class')

    # And able to successfully log out
    secure_page.logout()
    form_auth_page.verify_page_url()
    assert "success" in form_auth_page.get_status_banner().get_attribute('class')

# Test Case:
# Given on the Form Authentication page
# When submitting invalid credentials
# Then not logged in
# And receive error banner

def test_form_authentication_failed_login(page: Page):
    form_auth_page = FormAuthPage(page)
    
    # Given on the Form Authentication page
    form_auth_page.visit()

    # When submitting invalid credentials
    form_auth_page.login('invalid', 'invalid')

    # Then not logged in
    form_auth_page.verify_page_url()

    # And receive error banner
    assert "error" in form_auth_page.get_status_banner().get_attribute('class')