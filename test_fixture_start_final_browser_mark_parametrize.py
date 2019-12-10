import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print('\nsratr browser for test..')
    driver = webdriver.Firefox()
    yield driver
    print('\nquit browser..')
    driver.quit()

@pytest.mark.parametrize('language',['ru','en-gb'])
def test_guest_should_see_loginlink(browser,language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/'
    browser.get(link)
    browser.find_element_by_css_selector('#login_link')