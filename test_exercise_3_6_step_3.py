import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

result_text = []


@pytest.fixture(scope="function")
def browser():
    print('\nstart browser..')
    driver = webdriver.Firefox()
    yield driver
    print('\nquit browser..')
    driver.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
def test_collect_errors_by_response(browser,link):
    cur_link = f"{link}"
    browser.get(cur_link)
    browser.implicitly_wait(5)

    answer = str(math.log(int(time.time())))

    text_element = WebDriverWait(browser,5).until(EC.visibility_of(browser.find_element_by_css_selector('textarea')))
    text_element.send_keys(answer)

    browser.find_element_by_css_selector('button').click()

    hint_text = WebDriverWait(browser,5).until(EC.visibility_of(browser.find_element_by_css_selector('.smart-hints__hint'))).text

    if 'Correct!' != hint_text:
        result_text.append(hint_text)
        if cur_link == 'https://stepik.org/lesson/236905/step/1':
            print_answer()


def print_answer():
    print('\nRESULT:')
    print(*result_text, sep=' ')




