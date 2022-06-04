import time

from faker import Faker
from selenium.webdriver.common.by import By

from pages_object.basePage import BasePage
from support import wait_element


class RegisterPage(BasePage):
    TITlE = "Register Account"
    TAB = (By.XPATH, "//ul[@class='breadcrumb']/li[last()]")  # Register
    HEADER = (By.XPATH, "//div[@id='content']/h1")  # Register Account
    INPUT_FIRSTNAME = (By.XPATH, "//input[@name = 'firstname']")
    INPUT_LASTNAME = (By.XPATH, "//input[@name = 'lastname']")
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'email']")
    INPUT_TELEPHONE = (By.XPATH, "//input[@name = 'telephone']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    PASSWORD = "password123"
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
    YES_OPTION = (By.XPATH, "//label[@class='radio-inline']/input[@type='radio' and @value='1']")
    NO_OPTION = (By.XPATH, "//label[@class='radio-inline']/input[@type='radio' and @value='0']")
    CHECKBOX_PRIVACY_POLICY = (By.XPATH, "//input[@type='checkbox']")
    VERIFY_ACCOUNT_CREATED_TEXT = (By.XPATH, "//h1[contains(text(), 'Your Account Has Been Created!')]")

    def __init__(self, driver, base_url="") -> None:
        super().__init__(driver, base_url)

    def fullfill_form(self):
        f = Faker()
        wait_element(self.driver, self.INPUT_FIRSTNAME).send_keys(f.first_name())
        wait_element(self.driver, self.INPUT_LASTNAME).send_keys(f.last_name())
        wait_element(self.driver, self.INPUT_EMAIL).send_keys(f.email())
        wait_element(self.driver, self.INPUT_TELEPHONE).send_keys(f.phone_number())
        wait_element(self.driver, self.INPUT_PASSWORD).send_keys(self.PASSWORD)
        wait_element(self.driver, self.INPUT_PASSWORD_CONFIRM).send_keys(self.PASSWORD)
        return self

    def click_submit_button(self):
        wait_element(self.driver, self.SUBMIT_BUTTON).click()
        return self

    def submit_Subscribe(self):
        self.driver.find_element(*self.YES_OPTION).click()
        return self

    def click_checkbox_privacy_policy(self):
        wait_element(self.driver, self.CHECKBOX_PRIVACY_POLICY).click()
        return self

    def verify_account_has_been_created(self):
        wait_element(self.driver, self.VERIFY_ACCOUNT_CREATED_TEXT, time=10)
        return self
