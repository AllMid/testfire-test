from Pages.GooglePages import SearchHelper

def test_google_sql_injections_passwd(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_username("admin")
    google_auth_page.enter_word_password("' or 1=1--+")
    google_auth_page.click_on_the_login_button()
    assert browser.current_url == "http://testfire.net/login.jsp"