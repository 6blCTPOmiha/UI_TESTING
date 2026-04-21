import allure
from helpers.base_page import BasePage
from data.w2a_data.locators import Locators
from config.w2a_config import Config, Endpoints


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL + Endpoints.LOGIN


    @allure.step('Открытие страницы')
    def open_page(self):
        self.open(self.url)
        self.wait_for_paige_load()

    @allure.step('Ожидание загрузки страницы')
    def wait_for_paige_load(self):
        self.wait_for_url('login')

    @allure.step("Ввод username'а")
    def input_username(self, username):
        field = self.find_element(Locators.USERNAME_FIELD)
        field.send_keys(f'{username}')

    @allure.step("Ввод пароля")
    def input_password(self, password):
        field = self.find_element(Locators.PASSWORD_FIELD)
        field.send_keys(f'{password}')

    @allure.step("Ввод описания username'а")
    def input_username_description(self, username_description):
        field = self.find_element(Locators.USERNAME_DESCRIPTION_FIELD)
        field.send_keys(f'{username_description}')

    @allure.step("Нажатие на кнопку login")
    def click_login_btn(self):
        btn = self.wait_until_btn_is_clickable(Locators.LOGIN_BTN)
        btn.click()

    @allure.step("Нажатие на гипертекст logout")
    def click_logout_hypertext(self):
        hypertext = self.find_element(Locators.LOGOUT_HYPERTEXT)
        hypertext.click()
