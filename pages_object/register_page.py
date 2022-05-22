from selenium.webdriver.common.by import By


class RegisterPage:
    TITlE = "Register Account"
    TAB = (By.XPATH, "//ul[@class='breadcrumb']/li[last()]")  # Register
    HEADER = (By.XPATH, "//div[@id='content']/h1")  # Register Account
    INPUT_FIRSTNAME = (By.XPATH, "//input[@name = 'firstname']")
    INPUT_LASTNAME = (By.XPATH, "//input[@name = 'lastname']")
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'email']")
    INPUT_TELEPHONE = (By.XPATH, "//input[@name = 'telephone']")
