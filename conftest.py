import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.home.home_checks import HomeChecks
from pages.home.home_page import HomePage
from pages.membership.membership_checks import MembershipChecks
from pages.membership.membership_page import MembershipPage
from pages.login.login_checks import LoginChecks
from pages.login.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


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


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def home_checks(driver):
    return HomeChecks(driver)


@pytest.fixture
def membership_page(driver):
    return MembershipPage(driver)


@pytest.fixture
def membership_checks(driver):
    return MembershipChecks(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def login_checks(driver):
    return LoginChecks(driver)
