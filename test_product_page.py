from .pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
   link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
   page = ProductPage(browser, link)                       # создаем объект класса MainPage, передаем в конструктор экземпляр драйвера и url адрес
   page.open()                                          # открываем страницу
   page.add_to_basket()
   page.solve_quiz_and_get_code()
   page.book_price()
   page.book_price_in_basket()
   page.book_price_and_basket_price_should_be_equal()


   # login_page = LoginPage(browser, browser.current_url) # создаем переменную с новым объектом LoginPage и обязательно передаем ему
   #                                                      # тот же самый объект драйвера для работы с браузером, а в качестве url передаем текущий адрес
   # login_page.should_be_login_page()                    # используем методы LoginPage
