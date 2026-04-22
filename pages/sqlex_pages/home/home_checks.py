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

    @allure.step('Проверка. Фокус НЕ на input')
    def check_no_focus_on_input(self):
        active = self.return_focus_part()
        assert active != "INPUT", "Фокус остался на input"

    @allure.step('Проверка. Страница имеет скролл')
    def check_page_has_scroll(self):
        flag = self.is_page_has_scroll()
        assert flag, "Страница не имеет скролла"
