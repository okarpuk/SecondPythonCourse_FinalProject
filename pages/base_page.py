from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage():                                 # базовая страница, от которой будут унаследованы все остальные классы

    def __init__(self, browser, url, timeout=10): # конструктор—метод, который вызывается, когда мы создаем объект
        self.browser = browser                    # В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
        self.url = url
        self.browser.implicitly_wait(timeout)     # и неявное ожидание длительностью 10 секунд


    def open(self):                             # метод открывает нужную страницу в браузере, используя метод get().
        self.browser.get(self.url)


    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK) # символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()


    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def is_element_present(self, how, what):    # Чтобы перехватывать исключение, нужна конструкция try/except
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


    def is_not_element_present(self, how, what, timeout=4): #метод, который проверяет, что элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False


    def is_disappeared(self, how, what, timeout=4): #метод, который проверяет, что элемент исчезает в теение указанного времени
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
