
from selenium.webdriver.common.by import By
# def test_header(driver, main_page_url):
#     driver.get(main_page_url)
#     assert "Your Store" == driver.title

def test_menu(driver, main_page_url):
    driver.get(main_page_url)
    els = driver.find_elements(by = By.CSS_SELECTOR, value = ".dropdown")
    [print(type(el)) for el in els]


















