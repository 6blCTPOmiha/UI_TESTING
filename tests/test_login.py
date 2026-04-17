import allure
import pytest
from data.constants import Constants


@allure.epic("UI")
class TestRun:

    @allure.feature("Login page")
    @allure.story("Login test")
    @allure.title("All fields exist and login button dis/enable")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    def test_page_loading(self, login_page, login_checks):
        login_page.open_page()
        login_checks.check_username_field_visible()
        login_checks.check_password_field_visible()
        login_checks.check_login_btn_disable()
        login_page.input_username(Constants.DEFAULT_USERNAME)
        login_page.input_password(Constants.DEFAULT_PASSWORD)
        login_page.input_username_description(Constants.DEFAULT_USERNAME_DESCRIPTION)
        login_checks.check_login_btn_enable()


    @allure.feature("Login page")
    @allure.story("Login test")
    @allure.title("Success logining in system")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    @pytest.mark.parametrize('username, password',
                             [('angular', 'password'),
                              ('a', 'p'),
                              ('username', 'test_pass')])
    def test_success_log_in(self, login_page, login_checks, username, password):
        login_page.open_page()
        login_page.input_username(username)
        login_page.input_password(password)
        login_page.input_username_description(Constants.DEFAULT_USERNAME_DESCRIPTION)
        login_page.click_login_btn()
        login_checks.check_login_success()


    @allure.feature("Login page")
    @allure.story("Login test")
    @allure.title("Failure logining in system")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    def test_error_log_in(self, login_page, login_checks):
        login_page.open_page()
        login_page.input_username(Constants.DEFAULT_USERNAME)
        login_page.input_password(Constants.DEFAULT_PASSWORD)
        login_page.input_username_description(Constants.DEFAULT_USERNAME_DESCRIPTION)
        login_page.click_login_btn()
        login_checks.check_login_error()


    @allure.feature("Login page")
    @allure.story("Logout test")
    @allure.title("Success logining out system")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    def test_success_log_out(self, login_page, login_checks):
        login_page.open_page()
        login_page.input_username(Constants.DEFAULT_USERNAME)
        login_page.input_password(Constants.DEFAULT_PASSWORD)
        login_page.input_username_description(Constants.DEFAULT_USERNAME_DESCRIPTION)
        login_page.click_login_btn()
        login_page.click_logout_hypertext()
        login_checks.check_logout_success()
