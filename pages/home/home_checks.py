from helpers.base_page import BasePage
from data.locators import Locators


class HomeChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.locators = Locators()


    def check_navigation_panel(self):
        assert self.is_element_on_screen(self.locators.NAVIGATION_PANEL)


    def check_reg_btn(self):
        el = self.find_elements(self.locators.REGISTER_BTN)
        assert len(el) > 0, "No elements found"

    def check_list_of_courses(self):
        el = self.find_element(self.locators.BEST_SELENIUM_COURSE)
        assert el.is_displayed()

    def check_tel_number_ind(self):
        number = self.find_element(self.locators.HEADER_IND_NUMBER)
        assert number.text == '+919711-111-558'


    def check_tel_number_wa(self):
        number = self.find_element(self.locators.HEADER_WHATSUP_NUMBER)
        assert number.text == '+919711-191-558'


    def check_tel_number_usa(self):
        number = self.find_element(self.locators.HEADER_USA_NUMBER)
        assert number.text == '+1 646-480-0603'


    def check_skype(self):
        skype = self.find_element(self.locators.HEADER_SKYPE_ID)
        assert skype.text == 'seleniumcoaching'


    def check_top_email(self):
        email = self.find_element(self.locators.HEADER_EMAIL)
        assert email.text == 'trainer@way2automation.com'


    def check_facebook(self):
        facebook = self.find_element(self.locators.HEADER_FACEBOOK)
        assert facebook.is_displayed()


    def check_linkedin(self):
        linkedin = self.find_element(self.locators.HEADER_LINKEDIN)
        assert linkedin.is_displayed()


    def check_google(self):
        google_plus = self.find_element(self.locators.HEADER_GOOGLE)
        assert google_plus.is_displayed()


    def check_youtube(self):
        youtube = self.find_element(self.locators.HEADER_YOUTUBE)
        assert youtube.is_displayed()


    def check_footer_address(self):
        address = self.find_element(self.locators.FOOTER_ADDRESS)
        assert address.is_displayed()


    def check_footer_tel_1(self):
        el = self.find_element(self.locators.FOOTER_TEL_1)
        assert el.is_displayed()


    def check_footer_tel_2(self):
        el = self.find_element(self.locators.FOOTER_TEL_2)
        assert el.is_displayed()


    def check_footer_email_1(self):
        el = self.find_element(self.locators.FOOTER_EMAIL_1)
        assert el.is_displayed()


    def check_footer_email_2(self):
        el = self.find_element(self.locators.FOOTER_EMAIL_2)
        assert el.is_displayed()
