import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.home.home_checks import HomeChecks
from pages.home.home_page import HomePage
from pages.membership.membership_checks import MembershipChecks
from pages.membership.membership_page import MembershipPage


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


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
