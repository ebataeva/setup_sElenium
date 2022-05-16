import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


from pages_object import main_page

def test_header(driver, main_page_url):
    driver.get(main_page_url)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(main_page.MainPage.LOGO))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(main_page.MainPage.SEARCH_BAR))
    WebDriverWait(driver, 4).until(EC.visibility_of_element_located(main_page.MainPage.SEARCH_BAR_BUTTON))
    WebDriverWait(driver, 4).until(EC.visibility_of_element_located(main_page.MainPage.SEARCH_BAR_BUTTON_CART))

def test_slide(driver, main_page_url):
    driver.get(main_page_url)
    WebDriverWait(driver, 3).until(EC.visibility_of_all_elements_located(main_page.MainPage.SLIDE_1))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(main_page.MainPage.SWIPE_PAGINATOR_BULLET_0)).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(main_page.MainPage.SWIPE_PAGINATOR_BULLET_1)).click()
    time.sleep(5)