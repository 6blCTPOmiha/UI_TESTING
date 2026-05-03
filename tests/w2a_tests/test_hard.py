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
        tabs_page.switch_to_tab(1)
        tabs_page.click_on_hypertext()
        tabs_checks.check_number_of_tabs(3)
