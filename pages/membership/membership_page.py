from helpers.base_page import BasePage
from data.locators import Locators


class MembershipPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.url = 'https://www.way2automation.com/lifetime-membership-club/'
        self.locators = Locators()

    def wait_for_page_load(self):
        self.wait_for_specific_element(self.locators.MEMBER_BG_IMG_ON_TOP)