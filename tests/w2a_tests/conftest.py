import pytest

from pages.w2a_pages.alert.alert_checks import AlertChecks
from pages.w2a_pages.alert.alert_page import AlertPage
from pages.w2a_pages.home.home_checks import HomeChecks
from pages.w2a_pages.home.home_page import HomePage
from pages.w2a_pages.membership.membership_checks import MembershipChecks
from pages.w2a_pages.membership.membership_page import MembershipPage
from pages.w2a_pages.login.login_checks import LoginChecks
from pages.w2a_pages.login.login_page import LoginPage
from pages.w2a_pages.dnd.dnd_page import DndPage
from pages.w2a_pages.dnd.dnd_checks import DndChecks
from pages.w2a_pages.tabs.tabs_page import TabsPage
from pages.w2a_pages.tabs.tabs_checks import TabsChecks


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


@pytest.fixture
def dnd_page(driver):
    return DndPage(driver)


@pytest.fixture
def dnd_checks(driver):
    return DndChecks(driver)


@pytest.fixture
def tabs_page(driver):
    return TabsPage(driver)


@pytest.fixture
def tabs_checks(driver):
    return TabsChecks(driver)


@pytest.fixture
def alert_page(driver):
    return AlertPage(driver)


@pytest.fixture
def alert_checks(driver):
    return AlertChecks(driver)
