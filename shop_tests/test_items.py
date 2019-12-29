import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_user_should_see_add_to_basket_button(browser):
    browser.get(link)
    #time.sleep(30)

    # Should be button for adding into basket
    assert browser.find_element_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")

