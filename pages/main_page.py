from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators

class MainPage(BasePage): # класс-наследник класса BasePage
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" # символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать

