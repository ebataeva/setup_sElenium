from selenium.webdriver.common.by import By


class MainPage:
    LOGO = (By.CSS_SELECTOR, "#logo")
    SEARCH_BAR = (By.CSS_SELECTOR, "#search")
    SEARCH_BAR_BUTTON = (By.CSS_SELECTOR, "#input-group-btn")
