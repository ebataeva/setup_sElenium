from support import wait_elements, wait_element, wait_title_contain
from pages_object import register_page
from faker import Faker

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
    wait_element(driver, register_page.RegisterPage.INPUT_TELEPHONE).send_keys(f.phone_number())

