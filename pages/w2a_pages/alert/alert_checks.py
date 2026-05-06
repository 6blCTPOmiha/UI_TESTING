import allure
from helpers.base_page import BasePage
from data.w2a_data.locators import Locators


class AlertChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Проверка. Введённый текст появился")
    def check_text_after_alert(self):
        text_field = self.find_element(Locators.TEXT_AFTER_ALERT)
        assert "text_for_alert" in text_field.text, f"Текст не корректный либо отсутствует. Полученный текст: {text_field.text}"
