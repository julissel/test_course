'''Class Base Page'''

import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        main_window = self.browser.current_window_handle
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12*math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        self.browser.switch_to.window(main_window)
        self.browser.implicitly_wait(15)
        try:
            WebDriverWait(self.browser,5).until(EC.alert_is_present(), 'Waiting for second alert')
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except TimeoutException:
            print("No second alert presented")