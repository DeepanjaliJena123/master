import unittest
from selenium.webdriver import Chrome
from google import GooglePage

class test_google(unittest.TestCase):
    def setUp(self):
        self.driver=Chrome("path")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.google.com/")
        self.google_page=GooglePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_gmail_link(self):
        self.google_page.wait_for_google_default_page()
        status=self.google_page.get_gmail_link().is_enabled()
        assert status==True
        self.google_page.get_gmail_link().click()
        url=self.driver.current_url
        assert "gmail" in url

    def test_search_textbox(self):
        self.google_page.wait_for_google_default_page()
        self.google_page.get_search_textbox().send_keys("python")
        actual_content=self.google_page.get_search_textbox().get_attribute("name")
        assert actual_content=="python"



