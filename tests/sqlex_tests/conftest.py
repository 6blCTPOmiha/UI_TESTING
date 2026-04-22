import pytest
from pages.sqlex_pages.home.home_page import HomePage
from pages.sqlex_pages.home.home_checks import HomeChecks


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def home_checks(driver):
    return HomeChecks(driver)
