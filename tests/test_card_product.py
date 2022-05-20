import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support import  wait_elements, wait_title_contain, wait_element
from pages_object import card_product_page

def test_page_title(driver, main_page_url):
    driver.get(f"{main_page_url}{card_product_page.Card_product.ENDPOINT}")
    wait_title_contain(driver, card_product_page.Card_product.TITLE)

def test_card_name(driver, main_page_url):
    driver.get(f"{main_page_url}{card_product_page.Card_product.ENDPOINT}")
    assert wait_element(driver, card_product_page.Card_product.CARD_NAME).text == card_product_page.Card_product.TITLE


def test_price(driver, main_page_url):
    driver.get(f"{main_page_url}{card_product_page.Card_product.ENDPOINT}")
    assert wait_element(driver, card_product_page.Card_product.PRICE).text == card_product_page.Card_product.PRICE_VALUE


def test_add_to_card(driver, main_page_url):
    driver.get(f"{main_page_url}{card_product_page.Card_product.ENDPOINT}")
    driver.maximize_window()
    wait_element(driver, card_product_page.Card_product.ADD_TO_CART_BUTTON).click()
    assert wait_element(driver, card_product_page.Card_product.ALERT_SUCCESS_WINDOW).text == card_product_page.Card_product.TEXT_ALERT

def test_tab_name(driver, main_page_url):
    driver.get(f"{main_page_url}{card_product_page.Card_product.ENDPOINT}")
    assert wait_element(driver, card_product_page.Card_product.TAB_NAME).text == card_product_page.Card_product.TITLE

