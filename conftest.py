import pytest
import allure
from factory.driver_factory import DriverFactory
from config.base_config import Config



@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    remote = request.config.getoption("--remote")
    grid_url = request.config.getoption("--grid-url")
    driver = DriverFactory.create_driver(browser=browser, remote=remote, grid_url=grid_url)
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--remote", action="store_true")
    parser.addoption("--grid-url", action="store", default=Config.GRID_URL)


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
