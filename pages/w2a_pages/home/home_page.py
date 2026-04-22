import allure
from helpers.base_page import BasePage
from data.w2a_data.locators import Locators
from config.w2a_config import Config, Endpoints


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.url = Config.BASE_URL + Endpoints.HOME


    @allure.step('Открыть главную страницу')
    def open_page(self):
        self.open(self.url)
        self.wait_for_url(Config.BASE_URL)

    @allure.step('Прокрутить вниз до футера')
    def scroll_to_the_footer(self):
        self.scroll_to_the_bottom(Locators.FOOTER_PART)

    @allure.step('Прокрутить немного вниз')
    def scroll_a_little_down(self):
        self.scroll_down(700)

    @allure.step('Нажать на все курсы')
    def click_on_all_courses(self):
        self.wait_for_element_visible_for_user(Locators.ALL_COURSES)
        self.click_element_by_locator(Locators.ALL_COURSES)

    @allure.step('Нажать на подписку')
    def click_on_lifetime_membership(self):
        self.wait_for_element_visible_for_user(Locators.LIFETIME_MEMBERSHIP)
        self.click_element_by_locator(Locators.LIFETIME_MEMBERSHIP)
