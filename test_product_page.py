import pytest
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
   link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
   page = ProductPage(browser, link)                       # создаем объект класса MainPage, передаем в конструктор экземпляр драйвера и url адрес
   page.open()                                          # открываем страницу
   page.add_to_basket()
   page.solve_quiz_and_get_code()
   page.book_price()
   page.book_price_in_basket()
   page.book_price_and_basket_price_should_be_equal()
   page.book_name_and_book_name_in_basket_should_be_equal()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
   page = ProductPage(browser, link)
   page.open()
   page.add_to_basket()
   page.solve_quiz_and_get_code()
   page.book_price()
   page.book_price_in_basket()
   page.book_price_and_basket_price_should_be_equal()
   page.book_name_and_book_name_in_basket_should_be_equal()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
   link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
   page = ProductPage(browser, link)
   page.open()
   page.add_to_basket()
   page.solve_quiz_and_get_code()
   page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
   link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
   page = ProductPage(browser, link)
   page.open()
   page.add_to_basket()
   page.solve_quiz_and_get_code()
   page.message_should_disappear()
