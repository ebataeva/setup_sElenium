from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def type_in(driver, locator, name):
    try:
        click_to_element(driver, locator)
        wait_element(driver, locator).send_keys(name)
    except:
        raise AssertionError(f"не смог ввести {name} в поле, извините")

def click_to_element(driver, locator):
    try:
        wait_element(driver, locator).click()
    except:
        raise AssertionError(f"не смог кликнуь по элементу с локатором  {locator}")

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


def wait_for_alert(driver, locator, time=3):
    try:
        WebDriverWait(driver, time).until(EC.alert_is_present())
    except:
        raise AssertionError(f"не дождался видимости элемента {locator} за {time} секунд")