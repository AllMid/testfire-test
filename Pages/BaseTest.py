from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#creating a base class in base page
class BasePage:                     

    #initialization of the web driver and the URL of the web resource
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://testfire.net/login.jsp"                     

    #search for a specific element of a web resource by locator
    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    #search for several specific elements of a web resource by locator
    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    #switching to an initialized URL using an initialized web driver
    def go_to_site(self):
        return self.driver.get(self.base_url)
    
    #creates a string alert_txt, where it is indicated that alert_no (missing), 
    #then a search is performed and, if alert is found, the string changes to allert_yes
    def get_alert_box(self):
        alert_txt = "alert_no"
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(), 'Timed out waiting for confirmation popup to appear')
            alert_txt = "alert_yes"
        finally:
            return alert_txt
        