from Pages.BaseTest import BasePage
from selenium.webdriver.common.by import By

#creating a class that stores locators
class GoogleSeacrhLocators:
    #localization of the search bar by id in the code of a web resource
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.ID, "query")
    #localization of the search button by xpath in the code of a web resource
    LOCATOR_GOOGLE_SEARCH_BUTTON = (By.XPATH, "//*[@id='frmSearch']/table/tbody/tr[1]/td[2]/input[2]")
    #localization of the username input string by id in the code of a web resource
    LOCATOR_GOOGLE_USERNAME_FIELD = (By.ID, "uid")
    #localization of the password input string by id in the code of a web resource
    LOCATOR_GOOGLE_PASSWORD_FIELD = (By.ID, "passw")
    #localization of the Login button by name in the code of a web resource
    LOCATOR_GOOGLE_LOGIN_BUTTON = (By.NAME, "btnSubmit")

#creating a subclass, with BasePage as the parent
class SearchHelper(BasePage):

    #entering in the "username" field
    def enter_word_username(self, word):
        search_field = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_USERNAME_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    #entering in the "password" field
    def enter_word_password(self, word):
        search_field = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_PASSWORD_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field
    
    #entering in the "search" field
    def enter_word_search(self, word):
        search_field = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    #clicks on the "Login" button
    def click_on_the_login_button(self):
        return self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_LOGIN_BUTTON,time=2).click()

    #clicks on the "Go" button
    def click_on_the_search_button(self):
        return self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_SEARCH_BUTTON).click()


