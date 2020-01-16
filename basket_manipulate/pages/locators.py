from typing import Tuple
from selenium.webdriver.common.by import By


class BasketPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "[class='price_color']")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)")
    BASKET_VALUE_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div:nth-child(2)")
    CLOSE_BASKET_VALUE_MESSAGE = (By.CSS_SELECTOR, "a.btn-info:nth-child(1)")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_linc_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    BASKET_ITEMS = (By.CSS_SELECTOR, "[class='basket-items']")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
