import allure
from helpers.base_page import BasePage
from data.httpwatch_data.locators import Locators


class AuthenticationChecks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Проверка. Изображение появилось")
    def check_img_after_alert(self):
        img = self.find_element(Locators.RESULT_IMG)
        src = img.get_attribute("src")
        assert src, "Изображение не появилось"
