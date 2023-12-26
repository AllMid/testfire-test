from Pages.GooglePages import SearchHelper

#the test goes to the site, enters a username in the username field, enters an xss injection in the password field,
#clicks the Login button and checks whether the transition to the user's web page has occurred or not
def test_google_xss_injections_passwd(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_username("admin")
    google_auth_page.enter_word_password("<script>alert(123)</script>")
    google_auth_page.click_on_the_login_button()
    assert browser.current_url == "https://testfire.net/login.jsp"

#the test goes to the site, enters an xss injection in the username field, enters a password in the password field,
#clicks the Login button and checks whether the transition to the user's web page has occurred or not
def test_google_xss_injections_uid(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_username("<script>alert(123)</script>")
    google_auth_page.enter_word_password("passwd")
    google_auth_page.click_on_the_login_button()
    assert browser.current_url == "https://testfire.net/login.jsp"

#the test goes to the site, enters an xss injection in the search bar, 
#clicks on the Go button, reads the alert content and checks it with the required
def test_google_xss_injections_search(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_search("<script>alert(123)</script>")
    google_auth_page.click_on_the_search_button()
    alert = google_auth_page.get_alert_text()
    assert alert != "123"