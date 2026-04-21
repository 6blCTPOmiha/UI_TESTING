from selenium.webdriver.common.by import By


class Locators:
    LOGIN_FIELD = (By.XPATH, '//input[@type="text" and @name="login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password" and @name="psw"]')
    LOGIN_BTN = (By.CSS_SELECTOR, '[name="subm1"]')
    TEST_NAME_A = (By.XPATH, '//a[@href="/personal.php" and @class="none"]')
