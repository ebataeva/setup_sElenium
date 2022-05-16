from selenium.webdriver.common.by import By


class MainPage:
    LOGO = (By.CSS_SELECTOR, "#logo")
    SEARCH_BAR = (By.CSS_SELECTOR, "#search")
    SEARCH_BAR_BUTTON = (By.CSS_SELECTOR, ".input-group-btn")
    SEARCH_BAR_BUTTON_CART = (By.CSS_SELECTOR, "#cart")
    SLIDE_1 = (By.CSS_SELECTOR, "#slideshow0")
    SWIPE_PAGINATOR_BULLET_0 = (By.CSS_SELECTOR, ".swiper-pagination-bullet")
    SWIPE_PAGINATOR_BULLET_1 = (By.XPATH, "//div[contains(@class, 'swiper-pagination-bullet')]")
