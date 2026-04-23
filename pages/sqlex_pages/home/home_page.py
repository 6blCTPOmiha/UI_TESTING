import allure
from helpers.base_page import BasePage
from data.sqlex_data.locators import Locators
from data.sqlex_data.text_data import TextData
from config.sqlex_config import Config


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.url = Config.BASE_URL

    @allure.step('Открыть главную страницу')
    def open_page(self):
        self.open(self.url)
        self.wait_for_url(Config.BASE_URL)

    @allure.step("Ввод username'а")
    def input_username(self, username=TextData.TEST_LOGIN):
        field = self.find_element(Locators.LOGIN_FIELD)
        field.send_keys(f'{username}')

    @allure.step("Ввод пароля")
    def input_password(self, password=TextData.TEST_PASSWORD):
        field = self.find_element(Locators.PASSWORD_FIELD)
        field.send_keys(f'{password}')

    @allure.step('Нажать на вход')
    def click_on_enter(self):
        self.wait_for_element_visible_for_user(Locators.LOGIN_BTN)
        self.click_element_by_locator(Locators.LOGIN_BTN)

    @allure.step('Сохранить куки')
    def save_cookies_in_file(self):
        self.save_cookies(TextData.COOKIES_PATH)

    @allure.step('Загрузить куки')
    def load_cookies_from_file(self):
        self.load_cookies(TextData.COOKIES_PATH)
        self.refresh_page()

    @allure.step('Убрать фокус')
    def remove_focus(self):
        self.driver.execute_script("document.activeElement.blur();")
