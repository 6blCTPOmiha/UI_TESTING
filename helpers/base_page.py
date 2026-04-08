from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def find_element(self, locator, timeout=10):
        return self.wait_for_specific_element(locator, timeout)


    def find_elements(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))

    def scroll_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def scroll_down(self, length):
        ActionChains(self.driver).scroll_by_amount(0, length).perform()

    def click_element_by_locator(self, locator, timeout=15):
        element = self.find_element(locator, timeout)
        element.click()


    def is_element_on_screen(self, locator, timeout=15):
        element = self.find_element(locator, timeout)
        result = self.driver.execute_script("""
        const rect = arguments[0].getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= window.innerHeight &&
            rect.right <= window.innerWidth);
        """, element)
        return result


    def is_element_visible(self, locator, timeout=15):
        """Проверить видимость элемента"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False


    def wait_for_specific_element(self, locator, timeout=15):
        """
        Ожидание конкретного элемента на странице
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Элемент '{locator[1]}' не найден за {timeout} секунд")


    def wait_for_element_visible_for_user(self, locator, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located(locator))
        wait.until(lambda driver: driver.execute_script("var r = arguments[0].getBoundingClientRect(); return r.top < window.innerHeight && r.bottom >= 0;",
                                                        element))
        return element


    def open(self, url):
        self.driver.get(url)
