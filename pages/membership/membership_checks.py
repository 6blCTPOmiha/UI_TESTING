from helpers.base_page import BasePage
from data.locators import Locators


class MembershipChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def check_title(self):
        self.find_element(Locators.MEMBER_BG_IMG_ON_TOP)
        title = self.find_element(Locators.LMC_TITLE)
        assert title.text == "LIFETIME MEMBERSHIP CLUB", 'Отсутствует заголовок'

