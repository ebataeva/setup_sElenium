from pages_object import catalog_page
from support import wait_title_contain, wait_element, wait_elements
from pages_object.catalog_page import Catalog


def test_check_header(driver, main_page_url):
    driver.get(f"{main_page_url}/laptop-notebook")
    wait_title_contain(driver, "Notebooks", 3)


def test_catalog_menu(driver, main_page_url):
    driver.get(f"{main_page_url}/laptop-notebook")
    el = wait_element(driver, catalog_page.Catalog.CATALOG_MENU)


def test_catalog_menu_amount(driver, main_page_url):
    driver.get(f"{main_page_url}/laptop-notebook")
    assert len(wait_elements(driver, catalog_page.Catalog.CATALOG_MENU)) == 10


def test_points_sort_by(driver, main_page_url):
    driver.get(f"{main_page_url}/laptop-notebook")
    assert Catalog(driver).get_points_sort_by_len() == 9


def test_points_limit_by(driver, main_page_url):
    driver.get(f"{main_page_url}/laptop-notebook")
    assert Catalog(driver).get_points_limit_by_len() == 5
