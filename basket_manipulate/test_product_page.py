import time
import pytest
from .pages.product_page import PageObjectBasket


main_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
link_1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link_2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_3 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95"


@pytest.mark.skip #(reason="Too many links in the test. Run only by demand. For running test put # in the begining of the string.")
@pytest.mark.parametrize('link', [pytest.param(f'{main_link}{x}', marks=pytest.mark.xfail) if x == 7 else f'{main_link}{x}' for x in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    time.sleep(1)

    product_name = page.guest_can_see_product_name()
    product_price = page.guest_can_see_product_price()

    page.guest_can_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)

    page.guest_can_see_correct_product_name_in_message(product_name)
    page.guest_can_see_correct_product_price_in_message(product_price)
    time.sleep(1)

    #page.should_see_success_message_after_adding_product_into_the_basket()
    #page.guest_can_close_success_message()
    #page.should_disappear_success_message()
    #time.sleep(1)
    #page.should_not_be_success_message()


# Negative checks
@pytest.mark.xfail(reason="this test is in development")
@pytest.mark.parametrize('link', [link_2])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    page.guest_can_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [link_2])
def test_guest_cant_see_success_message(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip(reason="this test is in development")
@pytest.mark.parametrize('link', [link_2])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    page.guest_can_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_disappear_success_message()


@pytest.mark.parametrize('link', [link_3])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', [link_3])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    page.go_to_login_page()
