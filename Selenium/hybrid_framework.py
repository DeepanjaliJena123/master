# import unittest
# from selenium.webdriver import Chrome
#
# class Title_s(unittest.TestCase):
#     def titleverif(self):
#         driver = Chrome
#         driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#         driver.implicitly_wait(30)
#         actual = driver.title
#         expected = "OrangeHRM"
#         if actual == expected:
#             print("tastecaase pass")
#         else:
#             print("fail")
#         driver.close()

#exa:2 go to google page verify title of the webpage

# import unittest
# from selenium.webdriver import Chrome
# class TestGoogle(unittest.TestCase):
#     def test_google_title(self):
#         driver=Chrome
#         driver.implicitly_wait(30)
#         driver.get("https://www.google.com/")
#         actual_title=driver.title
#         expected_title="Google"
#         if actual_title==expected_title:
#             print("pass")
#         else:
#             print("fail")
#         driver.close()

##exa:3 test script using assert statement
# import unittest
# from selenium.webdriver import Chrome
# class TestGoogle(unittest.TestCase):
#     def test_google_title(self):
#         driver=Chrome
#         driver.implicitly_wait(30)
#         driver.get("https://www.google.com/")
#         actual_title=driver.title
#         expected_title="Google"
#         assert actual_title==expected_title
#         driver.close()

####  pre n post condition
# import unittest
# from selenium.webdriver import Chrome
# class TestGoogle(unittest.TestCase):
#     def preCondition(self):
#         self.driver=Chrome
#         self.driver.implicitly_wait(30)
#         self.driver.get("https://www.google.com/")
#
#     def postCondition(self):
#         self.driver.close()
#
#     def test_google_title(self):
#         self.preCondition()
#         actual_title=self.driver.title
#         expected_title="Google"
#         assert actual_title==expected_title
#         self.postCondition()
#     def test_google_url(self):
#         self.preCondition()
#         actual_url=self.driver.current_url
#         expected_url="https://www.google.com/"
#         assert actual_url==expected_url
#         self.postCondition()

#exa:4 setup and teardown
# import unittest
# from selenium.webdriver import Chrome
# class TestGoogle(unittest.TestCase):
#     def setUp(self):
#         self.driver=Chrome
#         self.driver.implicitly_wait(30)
#         self.driver.get("https://www.google.com/")
#
#     def tearDown(self):
#         self.driver.close()

# exa:5 Page object model
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class GooglePage():
    def __init__(self,driver):
        self.driver=driver

    def wait_for_google_default_page(self):
        wait=WebDriverWait(driver=self.driver,timeout=30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_id("viewport")))

    def get_gmail_link(self):
        try:
            element=self.driver.find_element_by_link_text("Gmail")
        except:
            return None

    def get_images_link(self):
        try:
            return self.driver.find_element_by_name("q")
        except:
            return None


import unittest
from selenium.webdriver import Chrome
from ddd.google_page import Googlepage

class TestGoogleU13516(unittest.TestCase):
    def SetUp(self):
        self.driver = Chrome("path")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.google.com/")
        # init page object class
        self.google_page = GooglePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_gmail_link_tc132765(self):
        #go to google page
        self.google_page.wait_for_google_default_page()
        #get Gmail link and check it is enabled
        status=self.google_page.get_gmail_link().is_enabled()
        assert status==True
        #click on gmail and check URL contain "gmail" or not
        self.google_page.get_gmail_link().click()
        url=self.driver.current_url
        assert 'gmail' in url
    def test_search_textbox_tc132766(self):
        #go to google page
        self.google_page.wait_for_google_default_page()
        #get searcch textbox and enter java
        self.google_page.get_search_textbox().send_keys('java')
        #get content of textbox and verify
        actual_content=self.google_page.get_search_textbox().get_attribute('value')
        assert actual_content=='java'














