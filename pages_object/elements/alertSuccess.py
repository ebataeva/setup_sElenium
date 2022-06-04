from pages_object.basePage import BasePage


class Alerts(BasePage):

    def __init__(self, driver, base_url="") -> None:
        super().__init__(driver, base_url)

    def accept_allert(self):
        alert = self.driver.switch_to.alert
        alert.accept()


    def dismis_allert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()
