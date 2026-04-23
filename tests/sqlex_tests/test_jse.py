import allure
import pytest
from data.sqlex_data.text_data import TextData


@allure.epic("UI")
class TestCookies:
    @allure.feature("Home page")
    @allure.story("JavaScriptExecutor test")
    @allure.title("Change focus")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.jse
    def test_success_log_in(self, home_page, home_checks):
        home_page.open_page()
        home_page.input_username(TextData.TEST_LOGIN)
        home_page.input_password(TextData.TEST_PASSWORD)
        home_page.remove_focus()
        home_checks.check_no_focus_on_input()

    @allure.feature("Home page")
    @allure.story("JavaScriptExecutor test")
    @allure.title("Page has scroll")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.jse
    def test_page_has_scroll(self, home_page, home_checks):
        home_page.open_page()
        home_checks.check_page_has_scroll()

