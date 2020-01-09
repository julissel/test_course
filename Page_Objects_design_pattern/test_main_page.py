from Page_Objects_design_pattern.pages.main_page import MainPage
from Page_Objects_design_pattern.pages.login_page import LoginPage


def test_guest_can_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.should_be_login_link() # проверяем наличие объекта "ссылки" на странице

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
