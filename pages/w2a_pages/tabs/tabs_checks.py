import allure
from helpers.base_page import BasePage


class TabsChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Проверка. Количество вкладок корректное")
    def check_number_of_tabs(self, target):
        count = self.count_tabs()
        assert count == target, "Количество вкладок не корректное"
