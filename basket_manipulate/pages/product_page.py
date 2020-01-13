''' class PageObject'''

import time
from .base_page import BasePage
from .locators import BasketPageLocators


class PageObjectBasket(BasePage):
    # Adding to basket
    def guest_can_add_to_basket(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BUTTON_ADD)
        basket_button.click()
        time.sleep(1)

    # Ptoduct Name
    def guest_can_see_product_name(self):
        product_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        print(f'\nProduct name before adding to the basket: {product_name}')
        return product_name

    def guest_can_see_correct_product_name_in_message(self, product_name):
        product_message_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_message_name == product_name
        print(f'\nProduct name in message: {product_message_name}')

    # Product Price
    def guest_can_see_product_price(self):
        product_price = self.browser.find_element(*BasketPageLocators.PRICE_OF_PRODUCT).text
        print(f'\nPrice of product before adding to the basket: {product_price}')
        return product_price

    def guest_can_see_correct_product_price_in_message(self, product_price):
        product_message_price = self.browser.find_element(*BasketPageLocators.PRICE_IN_MESSAGE).text
        assert product_price == product_message_price
        print(f'\nProduct price in message {product_message_price}')