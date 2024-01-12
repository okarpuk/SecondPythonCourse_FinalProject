import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
   def test_guest_can_go_to_login_page(self, browser):
      link = "http://selenium1py.pythonanywhere.com"
      page = MainPage(browser, link)                       # создаем объект класса MainPage, передаем в конструктор экземпляр драйвера и url адрес
      page.open()                                          # открываем страницу
      page.go_to_login_page()
      login_page = LoginPage(browser, browser.current_url) # создаем переменную с новым объектом LoginPage и обязательно передаем ему
                                                           # тот же самый объект драйвера для работы с браузером, а в качестве url передаем текущий адрес
      login_page.should_be_login_page()                    # используем методы LoginPage

   def test_guest_should_see_login_link(self, browser):
      link = "http://selenium1py.pythonanywhere.com/"
      page = MainPage(browser, link)
      page.open()
      page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
   link = "http://selenium1py.pythonanywhere.com/"
   page = MainPage(browser, link)
   page.open()
   page.go_to_basket_page()
   basket_page = BasketPage(browser, browser.current_url)
   basket_page.should_be_empty_basket()
