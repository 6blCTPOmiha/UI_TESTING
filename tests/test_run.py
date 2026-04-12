class TestRun:

    def test_page_loading(self, home_page, home_checks):
        home_page.open_page()
        home_checks.check_header()
        home_checks.check_navigation_panel()
        home_checks.check_reg_btn()
        home_checks.check_list_of_courses()
        home_page.scroll_to_the_footer()
        home_checks.check_footer()


    def test_header(self, home_page, home_checks):
        home_page.open_page()
        home_checks.check_tel_number_ind()
        home_checks.check_tel_number_wa()
        home_checks.check_tel_number_usa()
        home_checks.check_skype()
        home_checks.check_top_email()
        home_checks.check_facebook()
        home_checks.check_linkedin()
        home_checks.check_google()
        home_checks.check_youtube()


    def test_footer(self, home_page, home_checks):
        home_page.open_page()
        home_page.scroll_to_the_footer()
        home_checks.check_footer_address()
        home_checks.check_footer_tel_1()
        home_checks.check_footer_tel_2()
        home_checks.check_footer_email_1()
        home_checks.check_footer_email_2()


    def test_navigation_menu_on_scroll(self, home_page, home_checks):
        home_page.open_page()
        home_checks.check_navigation_panel()
        home_page.scroll_a_little_down()
        home_checks.check_navigation_panel()
        home_page.scroll_a_little_down()
        home_checks.check_navigation_panel()


    def test_membership_page(self, home_page, membership_page, membership_checks):
        home_page.open_page()
        home_page.click_on_all_courses()
        home_page.click_on_lifetime_membership()
        membership_checks.check_title()
