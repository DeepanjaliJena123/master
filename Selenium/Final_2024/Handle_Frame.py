# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://demoqa.com/frames")
# driver.switch_to.frame("frame1")
# frame1=driver.find_element_by_xpath("//h1[@id='sampleHeading']")
# time.sleep(2)
# print(frame1.text)


################
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
left=driver.find_element_by_xpath("//body[contains(text(),'LEFT')]")
time.sleep(2)
print(left.text)

driver.switch_to.default_content()
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-middle")
middle=driver.find_element_by_xpath("//div[contains(text(),'MIDDLE')]")
print(middle.text)

driver.switch_to.default_content()
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-right")
right=driver.find_element_by_xpath("//body[contains(text(),'RIGHT')]")
print(right.text)

driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
bottom=driver.find_element_by_xpath("//body[contains(text(),'BOTTOM')]")
print(bottom.text)



