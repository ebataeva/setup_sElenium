from selenium.webdriver.common.by import By

class Catalog:
    HOMME_BUTTON = (By.XPATH, "//i[@class='fa fa-home']")
    CATALOG_MENU = (By.XPATH, "//div[@class = 'list-group']/*")
    SORT_BY = (By.XPATH, "//select[@id='input-sort']/*") #9
    LIMIT_BY = (By.XPATH, "//select[@id='input-limit']/*") #5
    COMPONENTS_BUTTON = (By.XPATH, "//div[@class = 'list-group']/*")

