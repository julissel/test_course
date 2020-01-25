'''Class LoginPage'''
from .base_page import BasePage
from .locators import BasePageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):

        # input email
        email_form = self.browser.find_element(*BasePageLocators.USER_EMAIL_ADDRESS)
        email_form.send_keys(email)

        # input password
        password_form = self.browser.find_element(*BasePageLocators.USER_PASSWORD)
        password_form.send_keys(password)
        password_confirm_form = self.browser.find_element(*BasePageLocators.USER_CONFIRM_PASSWORD)
        password_confirm_form.send_keys(password)

        # confirm registration
        register_button = self.browser.find_element(*BasePageLocators.CONFIRM_REGISTRATION)
        register_button.click()
