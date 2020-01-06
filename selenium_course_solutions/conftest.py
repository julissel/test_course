import pytest
from selenium import webdriver

'''
Type any of command bellow in terminal for choosing browser:
pytest -s -v --browser_name=chrome test_parser.py
pytest -s -v --browser_name=firefox test_parser.py
'''

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox', help='Chose browser: chrome or firefox')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        print("\nstart browser Chrome for test..")
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print("\nstart browser Firefox for test..")
        browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()
