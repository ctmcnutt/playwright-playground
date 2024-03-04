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
    assert add_remove_elements_page.get_added_elements_count() == 0

# Test Case:
# Given on the Add/Remove Elements page
# When clicking 'Add' button multiple times
# Then as many 'Delete' buttons are created
# And clicking all delete buttons will remove them

def test_add_remove_elements_multiple_elements(page):
    add_remove_elements_page = AddRemoveElementsPage(page)

    # This var determines amount of buttons to add/delete
    numElements = 10

    # Given on the Add/Remove Elements page
    add_remove_elements_page.visit()

    # When clicking 'Add' button multiple times
    # Then as many 'Delete' buttons are created
    for x in range(numElements):
        add_remove_elements_page.get_add_button().click()
        assert add_remove_elements_page.get_added_elements_count() == x+1
    
    # And clicking all delete buttons will remove them
    for x in range(numElements):
        add_remove_elements_page.get_delete_button().first.click()
        assert add_remove_elements_page.get_added_elements_count() == (numElements-1)-x
