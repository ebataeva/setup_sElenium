from pages_object.basePage import BasePage


def test_change_curency_to_usd(driver, main_page_url):
    BP = BasePage(driver)
    driver.get(main_page_url)
    BP.click_currency_button().click_currency_usd_button()
