from helpers.base_page import BasePage
from data.locators import Locators


class HomeChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.locators = Locators()


    def check_navigation_panel(self):
        assert self.is_element_on_screen(self.locators.NAVIGATION_PANEL), 'Отсутствует панель навигации'


    def check_reg_btn(self):
        el = self.find_elements(self.locators.REGISTER_BTN)
        assert len(el) > 0, 'Кнопка регистрации отсутствует'

    def check_list_of_courses(self):
        assert self.is_element_on_screen(self.locators.BEST_SELENIUM_COURSE), 'Список курсов отсутствует'


    def check_tel_number_ind(self):
        assert self.is_element_on_screen(self.locators.HEADER_IND_NUMBER), 'Телефон отсутствует'


    def check_tel_number_wa(self):
        assert self.is_element_on_screen(self.locators.HEADER_WHATSUP_NUMBER), 'Телефон отсутствует'


    def check_tel_number_usa(self):
        assert self.is_element_on_screen(self.locators.HEADER_USA_NUMBER), 'Телефон отсутствует'


    def check_skype(self):
        assert self.is_element_on_screen(self.locators.HEADER_SKYPE_ID), 'Скайп отсутствует'


    def check_top_email(self):
        assert self.is_element_on_screen(self.locators.HEADER_EMAIL), 'Электронная почта отсутствует'


    def check_facebook(self):
        assert self.is_element_on_screen(self.locators.HEADER_FACEBOOK), 'facebook отсутствует'


    def check_linkedin(self):
        assert self.is_element_on_screen(self.locators.HEADER_LINKEDIN), 'linkedin отсутствует'


    def check_google(self):
        assert self.is_element_on_screen(self.locators.HEADER_GOOGLE), 'google_plus отсутствует'


    def check_youtube(self):
        assert self.is_element_on_screen(self.locators.HEADER_YOUTUBE), 'youtube отсутствует'


    def check_footer_address(self):
        assert self.is_element_on_screen(self.locators.FOOTER_ADDRESS), 'Адрес отсутствует'


    def check_footer_tel_1(self):
        assert self.is_element_on_screen(self.locators.FOOTER_TEL_1), 'Первый контактный телефон отсутствует'


    def check_footer_tel_2(self):
        assert self.is_element_on_screen(self.locators.FOOTER_TEL_2), 'Второй контактный телефон отсутствует'


    def check_footer_email_1(self):
        assert self.is_element_on_screen(self.locators.FOOTER_EMAIL_1), 'Первая контактная электронная почта отсутствует'


    def check_footer_email_2(self):
        assert self.is_element_on_screen(self.locators.FOOTER_EMAIL_2), 'Вторая контактная электронная почта отсутствует'
