import get_elements

titleKey = "page-title"


def verify_title(page_name, current_title, ):
    expected = get_elements.return_element_data(page_name, titleKey)
    if expected[1] == current_title: # expected[0] is search by and expected[1] is value
        assert True
    else:
        print "%s did not match expected %s" % (current_title,expected[1])
        assert False
