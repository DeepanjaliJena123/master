#EXA
#SYNTAX: Python -m pytest filepath -s -v
#1
# import unittest
# from selenium.webdriver import Chrome
# class Test_Frame(unittest.TestCase):
#     def test_frame(self):
#         driver=Chrome()
#         driver.get("https://demoqa.com/frames")
#         actual_title=driver.title
#         expected_title="DEMOQA"
#         if actual_title==expected_title:
#             print("---pass---")
#         else:
#             print("---fail---")
#         driver.close()
#
#2
# import unittest
# from selenium.webdriver import Chrome,ActionChains
# class Test_Dragdrp(unittest.TestCase):
#     def test_dragdrp(self):
#         driver=Chrome()
#         driver.get("https://the-internet.herokuapp.com/drag_and_drop")
#         driver.maximize_window()
#         d = ActionChains(driver=driver)
#         source = driver.find_element_by_id('column-a')
#         Target = driver.find_element_by_id("column-b")
#         d.move_to_element(source).click_and_hold().move_to_element(Target).release().perform()
#         driver.close()


##Test script using assert statement
# import unittest
# from selenium.webdriver import Chrome
# class Test_frame():
#     def test_frames(self):
#         driver=Chrome()
#         driver.get("https://demoqa.com/frames")
#         actual_title = driver.title
#         expected_title = "DEMOQA"
#         assert actual_title==expected_title
#         driver.close()

