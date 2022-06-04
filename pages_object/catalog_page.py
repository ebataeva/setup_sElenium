from selenium.webdriver.common.by import By

from pages_object.basePage import BasePage
from support import wait_elements


class Catalog(BasePage):
    HOMME_BUTTON = (By.XPATH, "//i[@class='fa fa-home']")
    CATALOG_MENU = (By.XPATH, "//div[@class = 'list-group']/*")
    SORT_BY = (By.XPATH, "//select[@id='input-sort']/*") #9
    LIMIT_BY = (By.XPATH, "//select[@id='input-limit']/*") #5
    COMPONENTS_BUTTON = (By.XPATH, "//div[@class = 'list-group']/*")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def get_points_sort_by_len(self):
        return len(wait_elements(self.driver, self.SORT_BY))

    def get_points_limit_by_len(self):
        return len(wait_elements(self.driver, self.LIMIT_BY))