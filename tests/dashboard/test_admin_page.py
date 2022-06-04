import time


from pages_object.adminPage import AdminPage
from pages_object.dashboard_page import Dashboard, Products
from pages_object.elements.alertSuccess import Alerts


def test_add_to_catalog_as_admin(driver, main_page_url):
    login_admin_page = AdminPage(driver, base_url=main_page_url)
    dashboard = Dashboard(driver)
    products_page = Products(driver)
    login_admin_page.logIN_to_admin_page().type_name_to_input().type_password_to_input().click_login_button()
    dashboard.check_title().click_menu_catalog().click_menu_products().click_add_new_button()
    products_page.check_title().input_product_name().input_meta_tag().click_data_tab().input_data_Model().click_save_button()
    time.sleep(3)
    dashboard.find_element_by_filter_name()

    time.sleep(15)


def test_find_element(driver, main_page_url):
    login_admin_page = AdminPage(driver, base_url=main_page_url)
    dashboard = Dashboard(driver)
    login_admin_page.logIN_to_admin_page().type_name_to_input().type_password_to_input().click_login_button()
    dashboard.click_menu_catalog().click_menu_products().find_element_by_filter_name()


def test_delete_element(driver, main_page_url):
    login_admin_page = AdminPage(driver, base_url=main_page_url)
    dashboard = Dashboard(driver)
    alert = Alerts(driver)
    login_admin_page.logIN_to_admin_page().type_name_to_input().type_password_to_input().click_login_button()
    dashboard.click_menu_catalog().click_menu_products().find_element_by_filter_name().click_delete_founded_element()
    alert.accept_allert()
    dashboard.sure_no_element_by_filter_name()



def test_element_not_found(driver, main_page_url):
    login_admin_page = AdminPage(driver, base_url=main_page_url)
    dashboard = Dashboard(driver)
    login_admin_page.logIN_to_admin_page().type_name_to_input().type_password_to_input().click_login_button()
    dashboard.click_menu_catalog().click_menu_products().sure_no_element_by_filter_name()
