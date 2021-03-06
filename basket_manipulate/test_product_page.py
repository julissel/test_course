import time
import pytest
from .pages.product_page import PageObjectBasket
from .pages.login_page import LoginPage


link_0 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
link_1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link_2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_3 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95"
link_login = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope ="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, link_login)
        self.page.open()
        user_tmp_generated_word = str(time.time())
        user_email = user_tmp_generated_word[-9:-1] + "@tmpmail.com"
        user_password = str(user_tmp_generated_word[-1:1] + user_tmp_generated_word[0:-1])
        time.sleep(1)
        self.page.register_new_user(user_email, user_password)
        time.sleep(3)
        self.page.should_be_authorized_user()

    @pytest.mark.skip(reason="This test is not marked as 'need_review'.")
    @pytest.mark.parametrize('link', [link_3])
    def test_user_cant_see_success_message(self, browser, link):
        page = PageObjectBasket(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [link_1])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = PageObjectBasket(browser, link)
        page.open()
        time.sleep(1)
        product_name = page.guest_can_see_product_name()
        product_price = page.guest_can_see_product_price()
        page.guest_can_add_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(3)
        page.guest_can_see_correct_product_name_in_message(product_name)
        page.guest_can_see_correct_product_price_in_message(product_price)
        time.sleep(1)


@pytest.mark.need_review
@pytest.mark.parametrize('link', [link_1])
def test_guest_can_add_product_to_basket(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    time.sleep(1)
    product_name = page.guest_can_see_product_name()
    product_price = page.guest_can_see_product_price()
    page.guest_can_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.guest_can_see_correct_product_name_in_message(product_name)
    page.guest_can_see_correct_product_price_in_message(product_price)
    time.sleep(1)


@pytest.mark.skip(reason="Too many links in the test. Run only by demand. For running test put # in the begining of this string.")
@pytest.mark.parametrize('link', [pytest.param(f'{link_0}{x}', marks=pytest.mark.xfail) if x == 7 else f'{link_0}{x}' for x in range(10)])
def test_guest_can_add_product_to_basket_for_many_pages(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    time.sleep(1)
    product_name = page.guest_can_see_product_name()
    product_price = page.guest_can_see_product_price()
    page.guest_can_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.guest_can_see_correct_product_name_in_message(product_name)
    page.guest_can_see_correct_product_price_in_message(product_price)
    time.sleep(1)


# Negative checks
@pytest.mark.xfail(reason="this test is in development")
@pytest.mark.parametrize('link', [link_2])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    page.guest_can_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.skip(reason="This test is not marked as 'need_review'.")
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


@pytest.mark.skip(reason="This test is not marked as 'need_review'.")
@pytest.mark.parametrize('link', [link_3])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [link_3])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [link_1])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = PageObjectBasket(browser, link)
    page.open()
    page.guest_can_open_basket_page_from_product_page()
    time.sleep(1)
    page.basket_grid_is_empty()
    page.basket_is_empty_message()
