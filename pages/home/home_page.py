from helpers.base_page import BasePage
from data.locators import Locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.url = 'https://www.way2automation.com'

    def open_page(self):
        self.open(self.url)
        self.find_element(Locators.HOME_BG_IMG_ON_TOP)

    def scroll_to_the_footer(self):
        self.scroll_to_the_bottom(Locators.FOOTER_PART)

    def scroll_a_little_down(self):
        self.scroll_down(700)

    def wait_for_ad_load(self):
        self.find_element(Locators.CLOSE_AD_BTN)

    def wait_for_page_load(self):
        self.find_element(Locators.HOME_BG_IMG_ON_TOP)

    def wait_for_header_load(self):
        self.find_element(Locators.HEADER_PART)

    def wait_for_navig_load(self):
        self.wait_for_element_visible_for_user(Locators.NAVIGATION_PANEL)

    def wait_for_all_courses_dropdown_trigger_load(self):
        self.wait_for_element_visible_for_user(Locators.ALL_COURSES)

    def wait_for_lifetime_membership_btn_load(self):
        self.wait_for_element_visible_for_user(Locators.LIFETIME_MEMBERSHIP)

    def wait_for_footer_load(self):
        self.wait_for_element_visible_for_user(Locators.FOOTER_PART)

    def click_close_ad_btn(self):
        self.click_element_by_locator(Locators.CLOSE_AD_BTN)

    def click_on_all_courses(self):
        self.wait_for_element_visible_for_user(Locators.ALL_COURSES)
        self.click_element_by_locator(Locators.ALL_COURSES)

    def click_on_lifetime_membership(self):
        self.wait_for_element_visible_for_user(Locators.LIFETIME_MEMBERSHIP)
        self.click_element_by_locator(Locators.LIFETIME_MEMBERSHIP)
