import allure
from helpers.base_page import BasePage
from data.w2a_data.locators import Locators
from config.w2a_config import Config, Endpoints


class MembershipPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.url = Config.BASE_URL + Endpoints.MEMBERSHIP

    @allure.step('Открыть страницу подписки')
    def wait_for_page_load(self):
        self.find_element(Locators.MEMBER_BG_IMG_ON_TOP)
