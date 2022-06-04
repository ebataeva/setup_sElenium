import time

from selenium.webdriver.common.by import By

from pages_object.basePage import BasePage
from support import wait_element, wait_title_contain, type_in, find_element_inside_the_element_by, sure_no_element
from faker import Faker


class Dashboard(BasePage):

    def __init__(self, driver, base_url="") -> None:
        super().__init__(driver, base_url)

    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    TITLE = "Dashboard"
    PRODUCTS_BUTTON = (By.XPATH, "//ul[@id='collapse1']/li[2]")
    ADD_PRODUCT_BUTTON = (By.XPATH, "//div[@class='pull-right']/a[1]")
    FILTER_PANEL = (By.CSS_SELECTOR, "#filter-product")
    FILTER_NAME = (By.CSS_SELECTOR, "#input-name")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#button-filter")
    name = "name1"
    IN_SEARCH_RESULT = (By.XPATH, f"//*[@alt= '{name}']")
    CHECKBOX_WITH_NAME = (f"//tr/td[contains(text(), '{name}')]//preceding-sibling::td/input")
    DELETE_BUTTON = (By.XPATH, "//button[@data-original-title='Delete']")

    def check_title(self):
        wait_title_contain(self.driver, self.TITLE)
        return self

    def click_menu_catalog(self):
        wait_element(self.driver, self.MENU_CATALOG).click()
        return self

    def click_menu_products(self):
        wait_element(self.driver, self.PRODUCTS_BUTTON).click()
        return self

    def click_add_new_button(self):
        wait_element(self.driver, self.ADD_PRODUCT_BUTTON).click()
        return self

    def find_element_by_filter_name(self):
        # self.driver.find_element_by_css_selector(self.FILTER_PANEL[1]).find_element_by_css_selector(self.FILTER_NAME[1])
        find_element_inside_the_element_by(self.driver, self.FILTER_PANEL, self.FILTER_NAME).send_keys(self.name)
        self.click_filter_button()
        wait_element(self.driver, self.IN_SEARCH_RESULT)
        return self

    def sure_no_element_by_filter_name(self):
        el = find_element_inside_the_element_by(self.driver, self.FILTER_PANEL, self.FILTER_NAME)
        el.click()
        el.clear()
        el.send_keys(self.name)
        self.click_filter_button()
        sure_no_element(self.driver, self.IN_SEARCH_RESULT)
        return self

    def click_filter_button(self):
        wait_element(self.driver, self.FILTER_BUTTON).click()
        return self

    def click_delete_founded_element(self):
        self.driver.find_element_by_xpath(self.CHECKBOX_WITH_NAME).click()
        wait_element(self.driver, self.DELETE_BUTTON).click()
        return self


class Products(Dashboard):
    TITLE = "Products"
    INPUT_NAME = (By.CSS_SELECTOR, "#input-name1")
    INPUT_META_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title1")
    INPUT_DATA_MODEL = (By.CSS_SELECTOR, "#input-model")

    DATA_TAB = (By.XPATH, "//ul[@class='nav nav-tabs']/li[2]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def check_title(self):
        wait_title_contain(self.driver, self.TITLE)
        return self

    def input_product_name(self):
        type_in(self.driver, self.INPUT_NAME, self.name)
        return self

    def input_meta_tag(self):
        type_in(self.driver, self.INPUT_META_TAG_TITLE, self.name)
        return self

    def click_data_tab(self):
        wait_element(self.driver, self.DATA_TAB).click()
        return self

    def input_data_Model(self):
        type_in(self.driver, self.INPUT_DATA_MODEL, self.name)
        return self

    def click_save_button(self):
        wait_element(self.driver, self.SUBMIT_BUTTON).click()
        return self
