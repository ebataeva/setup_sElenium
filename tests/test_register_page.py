from pages_object.basePage import BasePage
from pages_object.register_page import RegisterPage
from support import wait_title_contain, wait_element, wait_elements
from pages_object import register_page
from faker import Faker
from selenium.webdriver.common.keys import Keys

import time

def test_header(driver, main_page_url):
    driver.get(f"{main_page_url}index.php?route=account/register")
    wait_title_contain(driver, register_page.RegisterPage.TITlE)
    assert wait_element(driver, register_page.RegisterPage.TAB).text == "Register"
    assert wait_element(driver, register_page.RegisterPage.HEADER).text == "Register Account"

def test_input_info_negative(driver, main_page_url):
    f = Faker()
    driver.get(f"{main_page_url}index.php?route=account/register")
    wait_element(driver, register_page.RegisterPage.INPUT_FIRSTNAME).send_keys(f.first_name())
    wait_element(driver, register_page.RegisterPage.INPUT_LASTNAME).send_keys(f.last_name())
    wait_element(driver, register_page.RegisterPage.INPUT_EMAIL).send_keys(f.email())
    wait_element(driver, register_page.RegisterPage.INPUT_TELEPHONE).send_keys("\u2764")  # отправить сердечко
    time.sleep(3)

def test_register_new_user(driver, main_page_url):
    driver.get(main_page_url)
    BP = BasePage(driver, base_url=main_page_url)
    BP.click_my_account_button().click_register_menu_button()
    reg_page = RegisterPage(driver)
    reg_page.fullfill_form().click_checkbox_privacy_policy().click_submit_button().verify_account_has_been_created()
    time.sleep(10)