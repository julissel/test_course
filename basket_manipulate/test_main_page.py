import time
import pytest
from .pages.basket_page import BasketPage

main_link = 'http://selenium1py.pythonanywhere.com'


@pytest.mark.parametrize('link', [main_link])
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = BasketPage(browser, link)
    page.open()
    page.guest_can_open_basket_page()
    page.basket_is_empty()
    page.empty_basket_message()
