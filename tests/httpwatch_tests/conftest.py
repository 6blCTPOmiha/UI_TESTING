import pytest

from pages.httpwatch_pages.authentication.authentication_page import AuthenticationPage
from pages.httpwatch_pages.authentication.authentication_checks import AuthenticationChecks


@pytest.fixture
def authentication_page(driver):
    return AuthenticationPage(driver)


@pytest.fixture
def authentication_checks(driver):
    return AuthenticationChecks(driver)
