import allure
from helpers.base_page import BasePage
from data.w2a_data.locators import Locators


class MembershipChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка. Наличие требуемой надписи в заголовке')
    def check_title(self):
        self.find_element(Locators.MEMBER_BG_IMG_ON_TOP)
        title = self.find_element(Locators.LMC_TITLE)
        assert title.text == "LIFETIME MEMBERSHIP CLUB", 'Отсутствует заголовок'
