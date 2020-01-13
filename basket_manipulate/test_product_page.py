import time
import pytest
from .pages.product_page import PageObjectBasket
main_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'

@pytest.mark.parametrize('link', [pytest.param(f'{main_link}{x}', marks=pytest.mark.xfail) if x == 7 else f'{main_link}{x}' for x in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = PageObjectBasket(browser, link)
    page.open()
    time.sleep(10)

    product_name = page.guest_can_see_product_name()
    product_price = page.guest_can_see_product_price()

    page.guest_can_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)

    page.guest_can_see_correct_product_name_in_message(product_name)
    page.guest_can_see_correct_product_price_in_message(product_price)
