from pages.file_upload import FileUploadPage

# Test Case:
# Given on the File Upload page
# When uploading a valid file
# Then successful file upload result


def test_file_upload_successful(page):
    file_upload_page = FileUploadPage(page)
    test_file = "Test.txt"

    # Given on the Add/Remove Elements page
    file_upload_page.visit()

    # When uploading a valid file
    file_upload_page.choose_file(test_file)
    file_upload_page.click_upload_button()

    # Then successful file upload result
    assert file_upload_page.get_result_output().is_visible()
    assert file_upload_page.get_result_output().inner_text() == test_file


# Test Case:
# Given on the File Upload page
# When clicking upload with no file
# Then receive error message


def test_file_upload_error(page):
    file_upload_page = FileUploadPage(page)

    # Given on the Add/Remove Elements page
    file_upload_page.visit()

    # When clicking upload with no file
    file_upload_page.click_upload_button()

    # Then receive error message
    assert file_upload_page.get_error_message().is_visible()
