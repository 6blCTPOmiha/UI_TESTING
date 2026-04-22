import allure
from helpers.base_page import BasePage
from data.w2a_data.locators import Locators


class HomeChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка. Наличие хедера')
    def check_header(self):
        self.wait_for_element_visible_for_user(Locators.HEADER_PART)
        assert self.wait_for_element_visible_for_user(Locators.HEADER_PART), 'хедер с контактной информацией отсутствует'

    @allure.step('Проверка. Наличие панели навигации')
    def check_navigation_panel(self):
        self.wait_for_element_visible_for_user(Locators.NAVIGATION_PANEL)
        assert self.is_element_on_screen(Locators.NAVIGATION_PANEL), 'Отсутствует панель навигации'

    @allure.step('Проверка. Наличие кнопки регистрации')
    def check_reg_btn(self):
        el = self.find_elements(Locators.REGISTER_BTN)
        assert len(el) > 0, 'Кнопка регистрации отсутствует'

    @allure.step('Проверка. Наличие списка курсов')
    def check_list_of_courses(self):
        assert self.is_element_on_screen(Locators.BEST_SELENIUM_COURSE), 'Список курсов отсутствует'

    @allure.step('Проверка. Наличие индийского номера телефона')
    def check_tel_number_ind(self):
        assert self.is_element_on_screen(Locators.HEADER_IND_NUMBER), 'Телефон отсутствует'

    @allure.step("Проверка. Наличие what's up-a")
    def check_tel_number_wa(self):
        assert self.is_element_on_screen(Locators.HEADER_WHATSUP_NUMBER), 'Телефон отсутствует'

    @allure.step('Проверка. Наличие американского номера телефона')
    def check_tel_number_usa(self):
        assert self.is_element_on_screen(Locators.HEADER_USA_NUMBER), 'Телефон отсутствует'

    @allure.step('Проверка. Наличие логина скайпа')
    def check_skype(self):
        assert self.is_element_on_screen(Locators.HEADER_SKYPE_ID), 'Скайп отсутствует'

    @allure.step('Проверка. Наличие электронной почты')
    def check_top_email(self):
        assert self.is_element_on_screen(Locators.HEADER_EMAIL), 'Электронная почта отсутствует'

    @allure.step('Проверка. Наличие facebook-a')
    def check_facebook(self):
        assert self.is_element_on_screen(Locators.HEADER_FACEBOOK), 'facebook отсутствует'

    @allure.step('Проверка. Наличие linkedin-а')
    def check_linkedin(self):
        assert self.is_element_on_screen(Locators.HEADER_LINKEDIN), 'linkedin отсутствует'

    @allure.step('Проверка. Наличие google_plus-а')
    def check_google(self):
        assert self.is_element_on_screen(Locators.HEADER_GOOGLE), 'google_plus отсутствует'

    @allure.step('Проверка. Наличие youtube-а')
    def check_youtube(self):
        assert self.is_element_on_screen(Locators.HEADER_YOUTUBE), 'youtube отсутствует'

    @allure.step('Проверка. Наличие футера')
    def check_footer(self):
        self.wait_for_element_visible_for_user(Locators.FOOTER_PART)
        assert self.is_element_on_screen(Locators.FOOTER_PART)

    @allure.step('Проверка. Наличие контактного адреса')
    def check_footer_address(self):
        self.wait_for_element_visible_for_user(Locators.FOOTER_PART)
        assert self.is_element_on_screen(Locators.FOOTER_ADDRESS), 'Адрес отсутствует'

    @allure.step('Проверка. Наличие первого контактного телефона')
    def check_footer_tel_1(self):
        assert self.is_element_on_screen(Locators.FOOTER_TEL_1), 'Первый контактный телефон отсутствует'

    @allure.step('Проверка. Наличие второго контактного телефона')
    def check_footer_tel_2(self):
        assert self.is_element_on_screen(Locators.FOOTER_TEL_2), 'Второй контактный телефон отсутствует'

    @allure.step('Проверка. Наличие первой электронной почты')
    def check_footer_email_1(self):
        assert self.is_element_on_screen(Locators.FOOTER_EMAIL_1), 'Первая контактная электронная почта отсутствует'

    @allure.step('Проверка. Наличие второй электронной почты')
    def check_footer_email_2(self):
        assert self.is_element_on_screen(Locators.FOOTER_EMAIL_2), 'Вторая контактная электронная почта отсутствует'
