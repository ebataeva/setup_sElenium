from selenium.webdriver.common.by import By

from pages_object.basePage import BasePage


class RegisterPage(BasePage):
    TITlE = "Register Account"
    TAB = (By.XPATH, "//ul[@class='breadcrumb']/li[last()]")  # Register
    HEADER = (By.XPATH, "//div[@id='content']/h1")  # Register Account
    INPUT_FIRSTNAME = (By.XPATH, "//input[@name = 'firstname']")
    INPUT_LASTNAME = (By.XPATH, "//input[@name = 'lastname']")
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'email']")
    INPUT_TELEPHONE = (By.XPATH, "//input[@name = 'telephone']")

    def __init__(self, driver, base_url) -> None:
        super().__init__(driver, base_url)




