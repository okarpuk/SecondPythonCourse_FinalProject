from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_goods_in_basket()
        self.empty_basket_text_should_be_correct()


    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS_FORM), "Goods are in the basket, but should not be"
        # print("There are no goods in the basket - as expected")


    def should_be_empty_basket_message(self):
        return self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text


    def empty_basket_text_should_be_correct(self):
        assert self.should_be_empty_basket_message() == "Your basket is empty. Continue shopping"
        # print("Empty basket case correct")
