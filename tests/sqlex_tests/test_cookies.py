import allure
import pytest
from data.sqlex_data.text_data import TextData


@allure.epic("UI")
class TestCookies:

    @allure.feature("Home page")
    @allure.story("Login test")
    @allure.title("Success logining in system")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.cookies
    def test_success_log_in(self, home_page, home_checks):
        home_page.open_page()
        home_page.input_username(TextData.TEST_LOGIN)
        home_page.input_password(TextData.TEST_PASSWORD)
        home_page.click_on_enter()
        home_checks.check_login_success()


    @allure.feature("Home page")
    @allure.story("Login test")
    @allure.title("Logining in system and save cookies")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.cookies
    def test_log_in_and_save_cookies(self, home_page, home_checks):
        home_page.open_page()
        home_page.input_username(TextData.TEST_LOGIN)
        home_page.input_password(TextData.TEST_PASSWORD)
        home_page.click_on_enter()
        home_checks.check_login_success()
        home_page.save_cookies_in_file()


    @allure.feature("Home page")
    @allure.story("Login test")
    @allure.title("Logining in system using cookies")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.cookies
    def test_log_in_using_cookies(self, home_page, home_checks):
        home_page.open_page()
        home_page.load_cookies_from_file()
        home_checks.check_login_success()
