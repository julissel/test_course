from Page_Objects_design_pattern.pages.main_page import MainPage
from Page_Objects_design_pattern.pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.go_to_login_page() # переходим на страницу авторизации/регистрации
    # Тестируем страницу авторизации/регистрации
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
