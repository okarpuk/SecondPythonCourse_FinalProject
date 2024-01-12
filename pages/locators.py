from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_NAME_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_PRICE_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")


class BasketPageLocators():
    BASKET_GOODS_FORM = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
