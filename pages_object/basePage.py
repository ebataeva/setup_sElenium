import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Добавление нового товара в разделе администратора.
# Удаление товара из списка в разделе администартора.
# Регистрация нового пользователя в магазине опенкарта.
# Переключение валют из верхнего меню опенкарта.


class BasePage:
    def __init__(self, driver, base_url = "") -> None:
        self.driver = driver
        self.base_url = base_url


