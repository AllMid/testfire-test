from Pages.GooglePages import SearchHelper

def test_google_sql_injections_passwd(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_username("admin")
    google_auth_page.enter_word_password("' or 1=1--+")
    google_auth_page.click_on_the_login_button()
    assert browser.current_url == "https://testfire.net/login.jsp"

def test_google_sql_injections_uid(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_username("admin' or 1=1--+")
    google_auth_page.enter_word_password("passwd")
    google_auth_page.click_on_the_login_button()
    assert browser.current_url == "https://testfire.net/login.jsp"

def test_google_sql_injections_search(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_search("' or 1=1--+")
    google_auth_page.click_on_the_search_button()
    assert browser.current_url == "https://testfire.net/search.jsp?query=%27+or+1%3D1--%2B"