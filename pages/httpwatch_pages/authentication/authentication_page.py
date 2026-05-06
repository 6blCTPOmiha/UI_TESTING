import allure
from helpers.base_page import BasePage
from config.httpwatch_config import Config, Endpoints
from data.httpwatch_data.locators import Locators
from data.httpwatch_data.constants import Constants


class AuthenticationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL + Endpoints.AUTH


    @allure.step('Открытие страницы')
    def open_page(self):
        self.open_with_basic_auth(self.url, Constants.DEFAULT_USERNAME, Constants.DEFAULT_PASSWORD)
        self.wait_for_url('authentication')

    @allure.step('Прокрутить вниз до кнопки DisplayImage')
    def scroll_to_the_display_btn(self):
        self.scroll_to_the_bottom(Locators.DISPLAY_IMG_BTN)

    @allure.step('Нажать на кнопку DisplayImage')
    def click_display_btn(self):
        self.click_element_by_locator(Locators.DISPLAY_IMG_BTN)
