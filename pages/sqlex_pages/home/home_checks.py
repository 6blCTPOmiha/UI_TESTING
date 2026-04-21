import allure
from helpers.base_page import BasePage
from data.sqlex_data.locators import Locators
from data.sqlex_data.text_data import TextData


class HomeChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Проверка. Вход в аккаунт успешный')
    def check_login_success(self):
        name = self.find_element(Locators.TEST_NAME_A)
        assert name.text == TextData.TEST_NAME, 'Не удалось авторизоваться'
