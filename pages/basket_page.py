from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_goods_in_basket()
        self.should_be_empty_basket_message()

    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), "Goods are in the basket, but should not be"
        print("There are no goods in the basket - as expected")


    def should_be_empty_basket_message(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
