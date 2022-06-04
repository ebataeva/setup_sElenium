import time

from pages_object.adminPage import AdminPage


def test_add_to_card_as_admin(driver, main_page_url):
    login_admin_page = AdminPage(driver, base_url=main_page_url)
    login_admin_page.logIN_to_admin_page().type_name_to_input()
    time.sleep(6)