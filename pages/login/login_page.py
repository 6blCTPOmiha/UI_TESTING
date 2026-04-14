import allure
from helpers.base_page import BasePage
from data.locators import Locators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.url = 'https://www.way2automation.com/angularjs-protractor/registeration/#/login'


    @allure.step('Открыть главную страницу')
    def open_page(self):
        self.open(self.url)
        self.find_element(Locators.TEXT_ALERT)

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
