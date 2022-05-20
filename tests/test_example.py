import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_header(driver, main_page_url):
    driver.get(main_page_url)
    WebDriverWait(driver, 3).until(EC.visibility_of_all_elements_located())
    driver.find_element(By.CSS_SELECTOR, "header")
    assert "Your Store" == driver.title


def test_menu(driver, main_page_url):
    driver.get(main_page_url)
    els = driver.find_elements(by=By.CSS_SELECTOR, value=".dropdown")
    [print(type(el)) for el in els]

def test_product(driver, main_page_url):
    driver.get(main_page_url)
