from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from config import Config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    def open(self, url) -> None:
        self.driver.get(url)

    def find_element(self, locator, timeout=Config.TIMEOUT) -> WebElement:
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException(f"Элемент '{locator[1]}' не найден за {timeout} секунд")

    def find_elements(self, locator) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def scroll_to_the_bottom(self, locator) -> None:
        while True:
            self.scroll_down(1000)
            if self.is_element_on_screen(locator, timeout=10):
                break

    def scroll_down(self, length) -> None:
        ActionChains(self.driver).scroll_by_amount(0, length).perform()

    def click_element_by_locator(self, locator, timeout=Config.TIMEOUT) -> None:
        element = self.find_element(locator, timeout)
        element.click()


    def is_element_on_screen(self, locator, timeout=Config.TIMEOUT) -> bool:
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


    def wait_for_element_visible_for_user(self, locator, timeout=Config.TIMEOUT) -> WebElement:
        """Ожидание видимости элемента по пикселям на мониторе"""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located(locator))
        wait.until(lambda driver: driver.execute_script("var r = arguments[0].getBoundingClientRect(); return r.top < window.innerHeight && r.bottom >= 0;", element))
        return element

    def wait_until_btn_is_clickable(self, locator, timeout=Config.SHORT_TIMEOUT) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        btn = wait.until(EC.element_to_be_clickable(locator))
        return btn

    def wait_for_url(self, url_part, timeout=Config.TIMEOUT) -> None:
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))
