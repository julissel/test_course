import time
from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def guest_can_open_basket_page(self):
        basket_button_on_main_page = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket_button_on_main_page.click()
        time.sleep(1)

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There is an item in the basket, but shoul not be."

    def empty_basket_message(self):
        message_in_empty_basket = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert "basket is empty" in message_in_empty_basket, "Text 'Your basket is empty.' is not contained in the basket message."
