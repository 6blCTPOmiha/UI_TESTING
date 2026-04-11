from helpers.base_page import BasePage
from data.locators import Locators


class MembershipChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.locators = Locators()


    def check_title(self):
        title = self.find_element(self.locators.LMC_TITLE)
        assert title.text == "LIFETIME MEMBERSHIP CLUB", 'Отсутствует заголовок'

