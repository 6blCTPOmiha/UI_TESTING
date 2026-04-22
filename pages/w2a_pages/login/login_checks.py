import allure
from helpers.base_page import BasePage
from data.w2a_data.locators import Locators


class LoginChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Проверка. Вход в аккаунт успешный')
    def check_login_success(self):
        self.wait_for_element_visible_for_user(Locators.SUCCESS_LOGIN_TEXT)
        assert self.is_element_on_screen(Locators.SUCCESS_LOGIN_TEXT), 'Не удалось авторизоваться'

    @allure.step('Проверка. Вход в аккаунт. Ошибка: неправильный юзернейм или пароль')
    def check_login_error(self):
        alert = self.wait_for_element_visible_for_user(Locators.ALERT_LOGIN_ERROR)
        assert alert.text == "Username or password is incorrect", 'Сообщение об ошибке не отображается'

    @allure.step('Проверка. Выход из аккаунта успешный')
    def check_logout_success(self):
        self.check_username_field_visible()
        self.check_password_field_visible()

    @allure.step('Проверка. Поле Username отображается')
    def check_username_field_visible(self):
        self.wait_for_element_visible_for_user(Locators.USERNAME_FIELD)
        assert self.is_element_on_screen(Locators.USERNAME_FIELD), 'Поле Username не отображается'

    @allure.step('Проверка. Поле Password отображается')
    def check_password_field_visible(self):
        self.wait_for_element_visible_for_user(Locators.PASSWORD_FIELD)
        assert self.is_element_on_screen(Locators.PASSWORD_FIELD), 'Поле Password не отображается'

    @allure.step('Проверка. Кнопка Login кликабельна')
    def check_login_btn_enable(self):
        btn = self.wait_until_btn_is_clickable(Locators.LOGIN_BTN)
        assert btn is not None, 'Кнопка Login не кликабельна'

    @allure.step('Проверка. Кнопка Login не кликабельна')
    def check_login_btn_disable(self):
        assert self.is_btn_not_clickable(Locators.LOGIN_BTN), 'Кнопка Login кликабельна'

