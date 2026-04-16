import allure
import pytest


@allure.epic("UI")
class TestRun:

    @allure.feature("Login page")
    @allure.story("Login test")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    @pytest.mark.parametrize('username, password',
                             [('angular', 'password'),
                              ('a', 'password'),
                              ('angular', 'p'),
                              ('a', 'p')])
    def test_page_loading(self, login_page, login_checks, username, password):
        login_page.open_page()
        login_page.input_username(username)
        login_page.input_password(password)
        login_page.input_username_description('username_description')
        login_page.click_login_btn()
        login_checks.check_login_success()


