from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class GooglePage():
    def __init__(self,driver):
        self.driver=driver
    def wait_for_google_default_page(self):
        wait=WebDriverWait(driver=self.driver,timeout=30)
        wait.until(expected_conditions.visibility_of)
        self.driver.find_element_by_id("Gmail")

    def get_gmail_link(self):
        try:
            element=self.driver.find_element_by_link_text("Gmail")
            return element
        except:
            return None

    def get_images_link(self):
        try:
            return self.driver.find_element_by_link_text("Images")
        except:
            return None

    def get_search_textbox(self):
        try:
            return self.driver.find_element_by_link_name("q")
        except:
            return None







