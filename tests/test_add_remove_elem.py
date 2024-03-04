from pages.add_remove_elem import AddRemoveElementsPage

# Test Case:
# Given on the Add/Remove Elements page
# When clicking 'Add' button
# Then new 'Delete' button is added
# And new button disappears upon click

def test_add_remove_elements_single_element(page):
    add_remove_elements_page = AddRemoveElementsPage(page)
    # Given on the Add/Remove Elements page
    add_remove_elements_page.visit()

    # When clicking 'Add' button
    add_remove_elements_page.get_add_button().click()

     #Then new 'Delete' button is added
    assert add_remove_elements_page.get_delete_button().is_visible()

    # And new button disappears upon click
    add_remove_elements_page.get_delete_button().click()
    assert add_remove_elements_page.get_delete_button().count() == 0
