import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Remote("http://localhost:4444", options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--remote", action="store_true")
    parser.addoption("--grid-url", action="store", default="http://localhost:4444/wd/hub")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = driver.get_screenshot_as_png()
            driver.save_screenshot("screenshots/fail.png")
            allure.attach(screenshot, name='screenshot_on_fail', attachment_type=allure.attachment_type.PNG)
