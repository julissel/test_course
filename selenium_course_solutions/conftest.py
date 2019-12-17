import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help='Chose browser: chrome or firefox')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        print("\nstart browser Chrome for test..")
        browser = webdriver.Chrome()
    elif browser_name =='firefox':
        print("\nstart browser Firefox for test..")
        browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()
