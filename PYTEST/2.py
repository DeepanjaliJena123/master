#prCondition and postCondition

# import unittest
# from selenium.webdriver import Chrome
# class Test_frame(unittest.TestCase):
#     def preCondition(self):
#         self.driver=Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.driver.get("https://demoqa.com/frames")
#     def postCondtion(self):
#         self.driver.close()
#
#     def test_frames(self):
#         self.preCondition()
#         actual_title = self.driver.title
#         expected_title = "DEMOQA"
#         assert actual_title == expected_title
#         self.postCondtion()
#     def test_url(self):
#         self.preCondition()
#         actual_url=self.driver.current_url
#         expected_url="https://demoqa.com/frames"
#         assert actual_url==expected_url
#         self.postCondtion()


##### Setup and TearDown

import unittest
from selenium.webdriver import Chrome
class Test_frame(unittest.TestCase):
    def setUp(self):
        self.driver=Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://demoqa.com/frames")
    def tearDown(self):
        self.driver.close()