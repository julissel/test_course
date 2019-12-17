'''
For rerun failed test save in Run/Debug configurations/Additional Arguments: --reruns int_number_of_reruns
or type in console" pytest -v --reruns int_number_of_reruns
'''

link = 'http://selenium1py.pythonanywhere.com/'


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector('#login_link')


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector('#magic_link')
