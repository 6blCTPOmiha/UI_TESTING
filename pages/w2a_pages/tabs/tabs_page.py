import allure
from helpers.base_page import BasePage
from data.w2a_data.locators import Locators
from config.w2a_config import Config, Endpoints


class TabsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL + Endpoints.TABS


    @allure.step('Открытие страницы')
    def open_page(self):
        self.open(self.url)
        self.wait_for_url('frames-and-windows')

    @allure.step("Перевести фокус на iframe")
    def focus_on_iframe(self):
        iframe = self.find_element(Locators.IFRAME_TABS)
        self.switch_to_frame(iframe)

    @allure.step("Нажать на гипертекст")
    def click_on_hypertext(self):
        self.click_element_by_locator(Locators.NEW_TAB_HYPERTEXT)

    @allure.step("Перейти на вкладку")
    def go_to_last_tab(self):
        last = self.count_tabs() - 1
        self.switch_to_tab(last)
