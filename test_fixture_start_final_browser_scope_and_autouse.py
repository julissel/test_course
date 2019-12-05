import time
import pytest
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture(scope="class")
def browser():
    print('\nstart Firefox for test..')
    driver = webdriver.Firefox()
    yield driver
    print('\nquit Firefox')
    driver.quit()

@pytest.fixture(autouse=True)
def find_current_data():
    print('\ncurrent time', time.time())


class TestFirstPage():
    # do not passing fixture "find_current_data" as a parameter

    def test_user_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('#login_link')

    def test_guest_should_see_basket_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')

