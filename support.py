import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element(driver, locator, time=3):
    try:
        return WebDriverWait(driver, time).until(EC.visibility_of_element_located((locator)))
    except:
        raise AssertionError(f"не дождался видимости элемента {locator} за {time} секунд")


def wait_elements(driver, locator, time=3):
    try:
        return WebDriverWait(driver, time).until(EC.visibility_of_all_elements_located((locator)))
    except:
        raise AssertionError(f"не дождался видимости элемента {locator} за {time} секунд")

def sure_no_element(driver, locator, time=3):
    try:
        return WebDriverWait(driver, time).until_not(EC.visibility_of_element_located((locator)))
    except:
        raise AssertionError(f" элемент {locator} присутствует")



def wait_title_contain(driver, title, time=3):
    try:
        WebDriverWait(driver, time).until(EC.title_contains((title)))
    except:
        raise AssertionError(f"вместо {title}  в названии страницы {driver.title}")
