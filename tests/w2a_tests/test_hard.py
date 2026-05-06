import allure
import pytest


@allure.epic("UI")
class TestHard:

    @allure.feature("Droppable page")
    @allure.story("Default functionality")
    @allure.title("Simple performance test")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.w2av2
    def test_drag_n_drop(self, dnd_page, dnd_checks):
        dnd_page.open_page()
        dnd_page.focus_on_iframe()
        dnd_page.move_draggable_item_to_droppable()
        dnd_checks.check_drop_success()

    @allure.feature("Tabs page")
    @allure.story("Default functionality")
    @allure.title("Simple performance test")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.w2av2
    def test_tabs(self, tabs_page, tabs_checks):
        tabs_page.open_page()
        tabs_page.focus_on_iframe()
        tabs_page.click_on_hypertext()
        tabs_checks.check_number_of_tabs(2)
        tabs_page.go_to_last_tab()
        tabs_page.click_on_hypertext()
        tabs_checks.check_number_of_tabs(3)


    @allure.feature("Alert page")
    @allure.story("Default functionality")
    @allure.title("Simple performance test")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.w2av2
    def test_alert(self, alert_page, alert_checks):
        alert_page.open_page()
        alert_page.click_on_input_alert()
        alert_page.focus_on_iframe()
        alert_page.trigger_alert()
        alert_page.fill_alert_with_text()
        # alert_page.focus_on_iframe()
        alert_checks.check_text_after_alert()
