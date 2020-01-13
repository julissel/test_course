import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')
    parser.addoption('--browser_name', action='store', default='firefox', help='Choose browser: chrome or firefox')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        print('\nStart browser Chrome for test..')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nStart browser Firefox for test..')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_language', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    #browser.implicitly_wait(5)
    yield browser
    print('\nQuit browser..')
    browser.quit()
