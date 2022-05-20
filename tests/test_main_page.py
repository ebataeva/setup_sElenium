import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages_object import main_page
from support import wait_elements, wait_title_contain, wait_element


def test_header(driver, main_page_url):
    driver.get(main_page_url)
    wait_element(driver, main_page.MainPage.LOGO)
    wait_element(driver, main_page.MainPage.SEARCH_BAR)
    wait_element(driver, main_page.MainPage.SEARCH_BAR_BUTTON)
    wait_element(driver, main_page.MainPage.SEARCH_BAR_BUTTON_CART)


def test_slide(driver, main_page_url):
    driver.get(main_page_url)
    wait_elements(driver, main_page.MainPage.SLIDE_1)
    wait_element(driver, main_page.MainPage.SWIPE_PAGINATOR_BULLET_0).click()
    wait_element(driver, main_page.MainPage.SWIPE_PAGINATOR_BULLET_1).click()
    wait_element(driver, main_page.MainPage.SWIPE_PAGINATOR_BULLET_0).click()


def test_products_count(driver, main_page_url):
    driver.get(main_page_url)
    assert len(wait_elements(driver, main_page.MainPage.PRODUCTS)) == 4


def test_prices(driver, main_page_url):
    driver.get(main_page_url)
    assert len(wait_elements(driver, main_page.MainPage.PRICES)) == 4


def test_product(driver, main_page_url):
    driver.get(main_page_url)
    wait_element(driver, main_page.MainPage.PRODUCT)
