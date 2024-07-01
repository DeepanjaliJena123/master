from selenium import webdriver
import time
from PIL import Image
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
window=driver.find_element_by_xpath("(//a[@target='_blank'])[1]")
window.click()
time.sleep(5)
# allwindows=driver.window_handles
# parent=allwindows[0]
# child=allwindows[1]
# driver.switch_to.window(parent)
# print(driver.title)               #for title print
# time.sleep(2)
# driver.switch_to.window(child)
# time.sleep(3)
# print(driver.title)
# #for taking screenshot
# driver.save_screenshot("abc.png")
# # Loading the image
# image = Image.open("abc.png")
# # Showing the image
# image.show()

#
# from selenium import webdriver
# import time
# from PIL import Image
# driver=webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")
# main_window=driver.find_element_by_xpath("(//a[@target='_blank'])[1]")
# main_window.click()
# time.sleep(5)
# allwindow=driver.window_handles
# parent=allwindow[0]
# child=allwindow[1]
# driver.switch_to.window(parent)
# print(driver.title)
# time.sleep(2)
# driver.switch_to.window(child)
# print(driver.title)
# time.sleep(2)
#
# driver.save_screenshot("abc.png")
# time.sleep(2)
# image=Image.open("abc.png")
# time.sleep(2)
# image.show()
# driver.close()