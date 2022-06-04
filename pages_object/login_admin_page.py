from selenium.webdriver.common.by import By

from pages_object.basePage import BasePage
from support import wait_element


class LoginAdminPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ALERT_DANGER = (By.XPATH, "//div[@class = 'alert alert-danger alert-dismissible']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".close")
    ALERT_DANGER_TEXT = "No match for Username and/or Password.\n×"

    def __init__(self, driver) -> None:
        super().__init__(driver)


    def click_login_button(self):
        wait_element(self.driver, self.LOGIN_BUTTON).click()
        return self