import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support import wait_element
# Добавление нового товара в разделе администратора.
# Удаление товара из списка в разделе администартора.
# Регистрация нового пользователя в магазине опенкарта.
# Переключение валют из верхнего меню опенкарта.


class BasePage:
    def __init__(self, driver, base_url = "") -> None:
        self.driver = driver
        self.base_url = base_url

    MY_ACCOUNT_BUTTON = (By.XPATH, "//a[@title='My Account']")
    REGISTER_MENU_BUTTON = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']/li/a[text()='Register']")
    CURRENCYES_BUTTON = (By.CSS_SELECTOR, ".btn-group")
    USD_BUTTON = (By.XPATH, "//button[@name='USD']")


    def click_currency_button(self):
        wait_element(self.driver, self.CURRENCYES_BUTTON).click()
        return self

    def click_currency_usd_button(self):
        wait_element(self.driver, self.USD_BUTTON).click()
        return self

    def click_my_account_button(self):
        wait_element(self.driver, self.MY_ACCOUNT_BUTTON).click()
        return self

    def click_register_menu_button(self):
        wait_element(self.driver, self.REGISTER_MENU_BUTTON).click()
        return self

