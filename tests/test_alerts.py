import json
import time
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from support import wait_elements, wait_element


def test_basic_alert(driver):
    driver.get("https://konflic.github.io/examples/pages/alerts.html")
    time.sleep(1)
    driver.find_element(By.ID, "confirm").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    # alert.dismiss()
    alert.accept()
    time.sleep(3)


def test_basic_switch(driver):
    driver.get("https://konflic.github.io/examples/pages/iframes.html")
    time.sleep(1)
    frames = wait_elements(driver, (By.CSS_SELECTOR, "iframe"))
    driver.switch_to.frame(frames[0])  # переключить контекст
    wait_element(driver, (By.NAME, "search")).send_keys("TEST")
    time.sleep(2)
    driver.switch_to.default_content()


def test_basic_switch_window(driver):
    driver.get("https://konflic.github.io/examples/pages/iframes.html")
    main_window = driver.current_window_handle
    driver.execute_script('window.open();')  # открывает новое окно
    WebDriverWait(driver, 2).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://ya.ru")
    driver.switch_to.window(main_window)
    time.sleep(3)


def test_cookie(driver):
    driver.get("https:/ya.ru")
    driver.add_cookie({"name ": "test", "value": "True"})
    cookies = driver.get_cookies()
    with open("my_data.json", "w") as file:
        # file.write(str(cookies))
        file.write(json.dumps(cookies, indent=4))


def test_editor(driver):
    driver.get("https://konflic.github.io/examples/editor/index.html")
    INPUT = (By.XPATH, "//input[@type='file']")
    # uploader = wait_element(driver, INPUT, 6)
    uploader = driver.find_element(value="file-uploader")
    uploader.send_keys("C:/otus/pic/zefir.jpg")
    time.sleep(5)
    uploader.screenshot("uploader.png")
