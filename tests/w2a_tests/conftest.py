import pytest
from pages.w2a_pages.home.home_checks import HomeChecks
from pages.w2a_pages.home.home_page import HomePage
from pages.w2a_pages.membership.membership_checks import MembershipChecks
from pages.w2a_pages.membership.membership_page import MembershipPage
from pages.w2a_pages.login.login_checks import LoginChecks
from pages.w2a_pages.login.login_page import LoginPage


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
