from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException(f"Элемент '{locator[1]}' не найден за {timeout} секунд")

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def scroll_to_the_bottom(self, locator):
        while True:
            self.scroll_down(1000)
            if self.is_element_on_screen(locator, timeout=10):
                break

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


    def wait_for_element_visible_for_user(self, locator, timeout=15):
        """Ожидание видимости элемента по пикселям на мониторе"""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located(locator))
        wait.until(lambda driver: driver.execute_script("var r = arguments[0].getBoundingClientRect(); return r.top < window.innerHeight && r.bottom >= 0;", element))
        return element
