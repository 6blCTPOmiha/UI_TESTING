import allure
import pytest


@allure.epic("UI")
class TestHard2:

    @allure.feature("Authentication page")
    @allure.story("Default functionality")
    @allure.title("Simple performance test")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.w2av22
    def test_auth(self, authentication_page, authentication_checks):
        authentication_page.open_page()
        authentication_page.scroll_to_the_display_btn()
        authentication_page.click_display_btn()
        authentication_checks.check_img_after_alert()
