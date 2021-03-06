import pytest
from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome"
    )
    parser.addoption(
        "--drivers",
        default="C:\Otus\drivers"

    )
    parser.addoption(
        "--mainpage",
        default="http://192.168.1.76:8081/"

    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    if browser_name == "chrome":
        browser = webdriver.Chrome(executable_path=f"{drivers}\chromedriver.exe")
    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=f"{drivers}\geckodriver.exe")
    elif browser_name == "opera":
        browser = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        raise ValueError("Browser not supported")
    request.addfinalizer(browser.close)
    return browser


@pytest.fixture()
def main_page_url(request):
    return request.config.getoption("--mainpage")
