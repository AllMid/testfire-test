from Pages.GooglePages import SearchHelper

#the test goes to the site, enters a username in the username field, enters an sql injection in the password field,
#clicks the Login button and checks whether the transition to the user's web page has occurred or not
def test_google_sql_injections_passwd(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_username("admin")
    google_auth_page.enter_word_password("' or 1=1--+")
    google_auth_page.click_on_the_login_button()
    assert browser.current_url == "https://testfire.net/login.jsp"

#the test goes to the site, enters an sql injection in the username field, enters a password in the password field,
#clicks the Login button and checks whether the transition to the user's web page has occurred or not
def test_google_sql_injections_uid(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_username("admin' or 1=1--+")
    google_auth_page.enter_word_password("passwd")
    google_auth_page.click_on_the_login_button()
    assert browser.current_url == "https://testfire.net/login.jsp"

#the test goes to the site, enters an sql injection in the search bar, clicks on the Go button and checks the address of the web page
def test_google_sql_injections_search(browser):
    google_auth_page = SearchHelper(browser)
    google_auth_page.go_to_site()
    google_auth_page.enter_word_search("' or 1=1--+")
    google_auth_page.click_on_the_search_button()
    assert browser.current_url == "https://testfire.net/search.jsp?query=%27+or+1%3D1--%2B"