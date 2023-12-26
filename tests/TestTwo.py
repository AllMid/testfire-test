from Pages.GooglePages import SearchHelper

def test_google_xss_injections_passwd(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_username("admin")
    google_auth_page.enter_word_password("<script>alert(123)</script>")
    google_auth_page.click_on_the_login_button()
    assert browser.current_url == "https://testfire.net/login.jsp"

def test_google_xss_injections_uid(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_username("<script>alert(123)</script>")
    google_auth_page.enter_word_password("passwd")
    google_auth_page.click_on_the_login_button()
    assert browser.current_url == "https://testfire.net/login.jsp"

def test_google_xss_injections_search(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_search("<script>alert(123)</script>")
    google_auth_page.click_on_the_search_button()
    alert = google_auth_page.get_alert_text()
    assert alert != "123"