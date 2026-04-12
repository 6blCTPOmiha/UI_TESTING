import allure
from helpers.base_page import BasePage
from data.locators import Locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.url = 'https://www.way2automation.com'

    @allure.step('Открыть главную страницу')
    def open_page(self):
        self.open(self.url)
        self.find_element(Locators.HOME_BG_IMG_ON_TOP)

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
