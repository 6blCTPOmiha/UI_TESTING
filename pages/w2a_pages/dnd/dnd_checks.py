import allure
from helpers.base_page import BasePage
from data.w2a_data.locators import Locators


class DndChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Проверка. Перенос элемента успешный')
    def check_drop_success(self):
        droppable_item = self.find_element(Locators.DROPPABLE_ITEM)
        assert droppable_item.text == "Dropped!", 'Текст не изменился'
