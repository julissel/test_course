import pytest
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture(scope="function")
def browser():
    print('\nstart Firefox for test..')
    driver = webdriver.Firefox()
    yield driver
    print('\nquit Firefox..')
    driver.quit()


class TestFirstPage():
    @pytest.mark.smoke
    def test_user_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('#login_link')

    @pytest.mark.regression
    def test_guest_should_see_basket_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.find_element_by_css_selector('button.favorite')

''' In this project registration of marks performs in the file "pytest.ini". Another programmatically way is bellow.
def pytest_configure(config):
    config.addinivalue_line("markers", "env(name): mark test to run only on named environment")'''
