from selenium.webdriver.common.by import By

from pages_object.basePage import BasePage
from support import wait_element


class CardProduct(BasePage):
    TITLE = "HP LP3065"
    ENDPOINT = "laptop-notebook/hp-lp3065"
    CARD_NAME = (By.XPATH, "//div[@class='col-sm-4']/h1")
    PRICE = (By.XPATH, "//li/h2")
    PRICE_VALUE = "$122.00"
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    # ALERT_SUCCESS_WINDOW = (By.CSS_SELECTOR, ".alert alert-success alert-dismissible")
    ALERT_SUCCESS_WINDOW = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    TEXT_ALERT = f"Success: You have added {TITLE} to your shopping cart!\n×"
    TAB_NAME = (By.XPATH, "//*[@id='product-product']/ul/li[last()]/a")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_add_to_cart_button(self):
        return wait_element(self.driver, self.ADD_TO_CART_BUTTON).click()


