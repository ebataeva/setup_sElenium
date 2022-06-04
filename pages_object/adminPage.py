import json

from selenium.webdriver.common.by import By

from pages_object.basePage import BasePage
from support import wait_element, wait_elements, type_in


class AdminPage(BasePage):

    def __init__(self, driver, base_url=None) -> None:
        super().__init__(driver, base_url)

    USERNAME = "user"
    PASSWORD = "bitnami"
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def logIN_to_admin_page(self):
        self.driver.get(f"{self.base_url}admin")
        return self

    def type_name_to_input(self):
        type_in(self.driver, self.INPUT_USERNAME, self.USERNAME)
        return self

    def type_password_to_input(self):
        type_in(self.driver, self.INPUT_PASSWORD, self.PASSWORD)
        return self

    def click_login_button(self):
        wait_element(self.driver, self.LOGIN_BUTTON).click()
        return self

    def get_cookies_from_this_and_save(self):
        cookies = self.driver.get_cookies()
        with open("admin_cookies.json", "w") as file:
            file.write(json.dumps(cookies, indent=4))