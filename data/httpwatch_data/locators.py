from selenium.webdriver.common.by import By


class Locators:
    DISPLAY_IMG_BTN = (By.CSS_SELECTOR, '[id="displayImage"]')
    RESULT_IMG = (By.CSS_SELECTOR, '[id="downloadImg"]')
