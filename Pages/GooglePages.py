from Pages.BaseTestOne import BasePage
from selenium.webdriver.common.by import By

class GoogleSeacrhLocators:
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.ID, "query")
    LOCATOR_GOOGLE_SEARCH_BUTTON = (By.XPATH, "//*[@id='frmSearch']/table/tbody/tr[1]/td[2]/input[2]")
    LOCATOR_GOOGLE_USERNAME_FIELD = (By.ID, "uid")
    LOCATOR_GOOGLE_PASSWORD_FIELD = (By.ID, "passw")
    LOCATOR_GOOGLE_LOGIN_BUTTON = (By.NAME, "btnSubmit")
    LOCATOR_GOOGLE_MAIN_MESSAGE = (By.ID, "_ctl0__ctl0_Content_Main_message")

class SearchHelper(BasePage):

    def enter_word_username(self, word):
        search_field = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_USERNAME_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_word_password(self, word):
        search_field = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_PASSWORD_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field
    
    def enter_word_search(self, word):
        search_field = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_login_button(self):
        return self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_LOGIN_BUTTON,time=2).click()

    def click_on_the_search_button(self):
        return self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_SEARCH_BUTTON).click()

    def get_main_message(self):
        return self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_MAIN_MESSAGE)

