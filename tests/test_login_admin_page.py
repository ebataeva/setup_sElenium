from pages_object import login_admin_pages
from selenium.webdriver.common.by import By

def test_login_page_external(driver, main_page_url):
    driver.get(f"{main_page_url}admin")
    driver.find_element(*login_admin_pages.USERNAME_INPUT)
    driver.find_element(*login_admin_pages.PASSWORD_INPUT)
    driver.find_element(*login_admin_pages.SUBMIT_BUTTON)
    driver.find_element(*login_admin_pages.FORGOTTEN_PASSWORD)
    driver.find_element(*login_admin_pages.OPENCART_LINK)