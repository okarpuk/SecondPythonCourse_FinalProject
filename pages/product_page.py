import math
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): # класс-наследник класса BasePage
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")






    def book_price(self):
        book_cost = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_cost.text
        return

    def book_price_in_basket(self):
        book_cost_in_basket = (self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET))
        book_cost_in_basket.text
        return

    def book_price_and_basket_price_should_be_equal(self):
        assert self.book_price() == self.book_price_in_basket(), "Prices are not equal"
        print("Book price is equal to basket price")
