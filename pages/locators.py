from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.ID, "#id_login-username")
    LOGIN_PASSWORD = (By.ID, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login_form .btn")
    REGISTER_EMAIL = (By.ID, "#id_registration-email")
    REGISTER_PASSWORD = (By.ID, "#id_registration-password1")
    CONFIRM_REGISTER_PASSWORD = (By.ID, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register_form .btn")


