import allure
from helpers.base_page import BasePage
from config.w2a_config import Config, Endpoints
from data.w2a_data.locators import Locators
from data.w2a_data.constants import Constants


class AlertPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL + Endpoints.ALERT


    @allure.step('Открытие страницы')
    def open_page(self):
        self.open(self.url)
        self.wait_for_url('alert')

    @allure.step("Перейти в раздел Input Alert")
    def click_on_input_alert(self):
        self.click_element_by_locator(Locators.INPUT_ALERT_BTN)

    @allure.step("Перевести фокус на iframe")
    def focus_on_iframe(self):
        iframe = self.find_element(Locators.IFRAME_ALERT)
        self.switch_to_frame(iframe)

    @allure.step("Нажать на кнопку создания alert'а")
    def trigger_alert(self):
        self.click_element_by_locator(Locators.BUTTON_TO_ALERT)


    @allure.step("Заполнить alert")
    def fill_alert_with_text(self, text=Constants.DEFAULT_TEXT_FOR_ALERT):
        self.fill_alert(text)
