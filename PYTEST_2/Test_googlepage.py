
### Step to develop and create automation scripts #####
### Realtime Scenario
#user story id= U13516
#Testcase id: TC132765
#Description::verify google page
#step:
#1:go to google page
#2:verify gmail link is enabled or not
#3:click on gmail link and check URL contains Gmail or not

#Testcae:TC132766
#STEP:
#1:go to google page
#2: verify search textbox is enabled or not
#3:Enter Java and check content is displayed in textbox


import unittest
from selenium.webdriver import Chrome
from PYTEST.google_page import GooglePage
class TestGooglepage(unittest.TestCase):
    def setUp(self):
        self.driver=Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.google.com/")
        self.google_page=GooglePage(self.driver)
    def tearDown(self):
        self.driver.close()

    def test_gmail_link123(self):
        self.google_page.wait_for_google_default_page()
        status=self.google_page.get_gmail_link().is_enabled()

        assert status==True

        self.google_page.get_gmail_link().click()
        url=self.driver.current_url
        assert "gmail" in url

    def test_search_textbox145(self):
        self.google_page.wait_for_google_default_page()
        self.google_page.get_search_textbox().send_keys("Python")

        actual_content=self.google_page.get_search_textbox().get_attribute("Search")
        assert actual_content=="Python"


































