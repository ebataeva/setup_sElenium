
from pages_object import card_product_page
from pages_object.card_product_page import CardProduct
from support import wait_element, wait_title_contain


def test_page_title(driver, main_page_url):
    driver.get(f"{main_page_url}{card_product_page.CardProduct.ENDPOINT}")
    wait_title_contain(driver, card_product_page.CardProduct.TITLE)


def test_card_name(driver, main_page_url):
    driver.get(f"{main_page_url}{card_product_page.CardProduct.ENDPOINT}")
    assert wait_element(driver, card_product_page.CardProduct.CARD_NAME).text == card_product_page.CardProduct.TITLE


def test_price(driver, main_page_url):
    driver.get(f"{main_page_url}{card_product_page.CardProduct.ENDPOINT}")
    assert wait_element(driver, card_product_page.CardProduct.PRICE).text == card_product_page.CardProduct.PRICE_VALUE


def test_add_to_card(driver, main_page_url):
    driver.get(f"{main_page_url}{card_product_page.CardProduct.ENDPOINT}")
    driver.maximize_window()
    CardProduct(driver).click_add_to_cart_button()
    assert wait_element(driver,
                        card_product_page.CardProduct.ALERT_SUCCESS_WINDOW).text == card_product_page.CardProduct.TEXT_ALERT


def test_tab_name(driver, main_page_url):
    driver.get(f"{main_page_url}{card_product_page.CardProduct.ENDPOINT}")
    assert wait_element(driver, card_product_page.CardProduct.TAB_NAME).text == card_product_page.CardProduct.TITLE
