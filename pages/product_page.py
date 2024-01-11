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

    def book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def book_name_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text

    def book_name_and_book_name_in_basket_should_be_equal(self):
        assert self.book_name() == self.book_name_in_basket(), "Names are not equal"
        print("Book name is equal to basket name")

    def book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def book_price_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET).text

    def book_price_and_basket_price_should_be_equal(self):
        assert self.book_price() == self.book_price_in_basket(), "Prices are not equal"
        print("Book price is equal to basket price")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        print("Success message is not presented - as expected")

    def message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message is not disappear, but should"
        print("Message is disappeared - as expected")
