import allure
from helpers.base_page import BasePage
from data.w2a_data.locators import Locators
from config.w2a_config import Config, Endpoints


class DndPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL + Endpoints.DRAG_N_DROP


    @allure.step('Открытие страницы')
    def open_page(self):
        self.open(self.url)
        self.wait_for_url('droppable')

    @allure.step("Перевести фокус на iframe")
    def focus_on_iframe(self):
        iframe = self.find_element(Locators.IFRAME_DND)
        self.switch_to_frame(iframe)

    @allure.step("Перетащить элемент в принимающий")
    def move_draggable_item_to_droppable(self):
        draggable_item = self.find_element(Locators.DRAGGABLE_ITEM)
        droppable_item = self.find_element(Locators.DROPPABLE_ITEM)
        self.hold_move_release(draggable_item, droppable_item)
