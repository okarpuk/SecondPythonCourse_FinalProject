from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage): # класс-наследник класса BasePage
    def go_to_login_page(self): # аргумент self , чтобы иметь доступ к атрибутам и методам класса
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" # символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать