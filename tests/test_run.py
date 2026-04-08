from pages.home.home_page import HomePage
from pages.home.home_checks import HomeChecks
from pages.membership.membership_page import MembershipPage
from pages.membership.membership_checks import MembershipChecks


class TestRun:

    def test_page_loading(self, driver):
        home_page = HomePage(driver)
        home_checks = HomeChecks(driver)
        home_page.open_page()
        home_page.wait_for_page_load()
        home_checks.check_skype()
        home_checks.check_navigation_panel()
        home_checks.check_reg_btn()
        home_checks.check_list_of_courses()
        home_page.tp_down()
        home_page.wait_for_footer_load()
        home_checks.check_footer_tel_1()


    def test_header(self, driver):
        home_page = HomePage(driver)
        home_checks = HomeChecks(driver)
        home_page.open_page()
        home_page.wait_for_page_load()
        home_checks.check_tel_number_ind()
        home_checks.check_tel_number_wa()
        home_checks.check_tel_number_usa()
        home_checks.check_skype()
        home_checks.check_top_email()
        home_checks.check_facebook()
        home_checks.check_linkedin()
        home_checks.check_google()
        home_checks.check_youtube()


    def test_footer(self, driver):
        home_page = HomePage(driver)
        home_checks = HomeChecks(driver)
        home_page.open_page()
        home_page.wait_for_page_load()
        home_page.tp_down()
        home_page.wait_for_footer_load()
        home_checks.check_footer_address()
        home_checks.check_footer_tel_1()
        home_checks.check_footer_tel_2()
        home_checks.check_footer_email_1()
        home_checks.check_footer_email_2()


    def test_navigation_menu_on_scroll(self, driver):
        home_page = HomePage(driver)
        home_checks = HomeChecks(driver)
        home_page.open_page()
        home_page.wait_for_page_load()
        home_page.wait_for_navig_load()
        home_checks.check_navigation_panel()
        home_page.scroll_a_little_down()
        home_page.wait_for_navig_load()
        home_checks.check_navigation_panel()
        home_page.scroll_a_little_down()
        home_page.wait_for_navig_load()
        home_checks.check_navigation_panel()


    def test_3(self, driver):
        home_page = HomePage(driver)
        membership_page = MembershipPage(driver)
        membership_checks = MembershipChecks(driver)
        home_page.open_page()
        home_page.wait_for_page_load()
        home_page.wait_for_all_courses_dropdown_trigger_load()
        home_page.click_on_all_courses()
        home_page.wait_for_lifetime_membership_btn_load()
        home_page.click_on_lifetime_membership()
        membership_page.wait_for_page_load()
        membership_checks.check_title()
