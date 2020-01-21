''' class PageObjectBasket'''

import time
from .base_page import BasePage
from .locators import BasePageLocators


class PageObjectBasket(BasePage):
    # Adding to basket
    def guest_can_add_to_basket(self):
        basket_button = self.browser.find_element(*BasePageLocators.BUTTON_ADD)
        basket_button.click()
        time.sleep(1)

    # View basket
    def guest_can_open_basket_page_from_product_page(self):
        basket_button_on_product_page = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_button_on_product_page.click()
        time.sleep(1)

    # Ptoduct Name
    def guest_can_see_product_name(self):
        product_name = self.browser.find_element(*BasePageLocators.PRODUCT_NAME).text
        print(f'\nProduct name before adding to the basket: {product_name}')
        return product_name

    # Product Name after successful adding into basket
    def guest_can_see_correct_product_name_in_message(self, product_name):
        product_message_name = self.browser.find_element(*BasePageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_message_name == product_name
        print(f'\nProduct name in message: {product_message_name}')

    # Product Price
    def guest_can_see_product_price(self):
        product_price = self.browser.find_element(*BasePageLocators.PRICE_OF_PRODUCT).text
        print(f'\nPrice of product before adding to the basket: {product_price}')
        return product_price

    # Product Price after successful adding into basket
    def guest_can_see_correct_product_price_in_message(self, product_price):
        product_message_price = self.browser.find_element(*BasePageLocators.PRICE_IN_MESSAGE).text
        assert product_price == product_message_price
        print(f'\nProduct price in message {product_message_price}')


    # Checks for empty basket on basket page
    def basket_grid_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), "There is an item in the basket grid, but shoul not be."

    def basket_is_empty_message(self):
        message_in_empty_basket = self.browser.find_element(*BasePageLocators.BASKET_MESSAGE).text
        assert "basket is empty" in message_in_empty_basket, "Text 'Your basket is empty.' is not contained in the basket message."


    # Negative Checks for success message
    def should_see_success_message_after_adding_product_into_the_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_VALUE_MESSAGE), "No success message after product was added into the basket"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*BasePageLocators.BASKET_VALUE_MESSAGE), "Success message is not dissapeared after product was added into the basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_VALUE_MESSAGE), "Success message is presented, but should not be"
