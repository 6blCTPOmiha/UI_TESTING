import allure
import pytest
from data.w2a_data.constants import Constants


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
