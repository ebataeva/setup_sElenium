from pages_object import login_admin_page
from selenium.webdriver.common.by import By
import time
from support import wait_element, wait_title_contain, wait_elements, sure_no_element


def test_login_page_external(driver, main_page_url):
    driver.get(f"{main_page_url}admin")
    wait_element(driver, login_admin_page.LoginAdminPage.USERNAME_INPUT)
    wait_element(driver, login_admin_page.LoginAdminPage.PASSWORD_INPUT)
    wait_element(driver, login_admin_page.LoginAdminPage.SUBMIT_BUTTON)
    wait_element(driver, login_admin_page.LoginAdminPage.FORGOTTEN_PASSWORD)
    wait_element(driver, login_admin_page.LoginAdminPage.OPENCART_LINK)


def test_click_login_negative(driver, main_page_url):
    driver.get(f"{main_page_url}admin")
    wait_element(driver, login_admin_page.LoginAdminPage.LOGIN_BUTTON).click()
    assert wait_element(driver,
                        login_admin_page.LoginAdminPage.ALERT_DANGER).text == login_admin_page.LoginAdminPage.ALERT_DANGER_TEXT
    wait_element(driver, login_admin_page.LoginAdminPage.CLOSE_BUTTON).click()
    sure_no_element(driver, login_admin_page.LoginAdminPage.CLOSE_BUTTON)
    time.sleep(5)
