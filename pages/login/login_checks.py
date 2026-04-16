import allure
from helpers.base_page import BasePage
from data.locators import Locators


class LoginChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Проверка. Вход в аккаунт')
    def check_login_success(self):
        self.wait_for_element_visible_for_user(Locators.TEXT_HOME)
        assert self.is_element_on_screen(Locators.TEXT_HOME), 'Не удалось авторизоваться'
