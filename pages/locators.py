from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    # LOGIN_EMAIL = (By.ID, "#id_login-username")
    # LOGIN_PASSWORD = (By.ID, "#id_login-password")
    # LOGIN_BUTTON = (By.CSS_SELECTOR, ".login_form .btn")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    # REGISTER_EMAIL = (By.ID, "#id_registration-email")
    # REGISTER_PASSWORD = (By.ID, "#id_registration-password1")
    # CONFIRM_REGISTER_PASSWORD = (By.ID, "#id_registration-password2")
    # REGISTER_BUTTON = (By.CSS_SELECTOR, ".register_form .btn")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_NAME_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_PRICE_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='111']")
    DISAPPEARED_MESSAGE = (By.XPATH, "//div[@id='112']")


