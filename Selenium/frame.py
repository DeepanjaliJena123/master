# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://demoqa.com/frames")
# # driver.switch_to.frame('frame1')
# frames=driver.find_element_by_xpath("//h1[@id='sampleHeading']")
# time.sleep(5)
# print(frames.text)    #for text print

####################################practice
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://demoqa.com/frames")
# driver.maximize_window()
# #1st have to switch frame
# driver.switch_to.frame('frame1')
# #then identify text locator for print frame text
# frame_text=driver.find_element_by_xpath("//div[@id='frame1Wrapper']")
# time.sleep(2)
# print(frame_text.text)
# driver.close()
# //h1[contains(text(),'This is a sample page')]

###############################################################



# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/nested_frames")
# driver.switch_to.frame("frame-top")
# driver.switch_to.frame("frame-left")
# frames=driver.find_element_by_xpath('//body')
# print(frames.text)
# time.sleep(2)
# driver.switch_to.default_content()
# driver.switch_to.frame("frame-top")
# driver.switch_to.frame("frame-middle")
# frames=driver.find_element_by_xpath('//body')
# print(frames.text)
# time.sleep(2)
# driver.switch_to.default_content()
# driver.switch_to.frame("frame-top")
# driver.switch_to.frame("frame-right")
# frames=driver.find_element_by_xpath('//body')
# print(frames.text)
# time.sleep(2)
# driver.switch_to.default_content()
# driver.switch_to.frame("frame-bottom")
# frames=driver.find_element_by_xpath('//body')
# print(frames.text)
# time.sleep(2)

# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/nested_frames")
# driver.maximize_window()
#1st switch top frame then switch left frame n find element locator of left frame n print laft frame inside text
# driver.switch_to.frame("frame-top")
# driver.switch_to.frame("frame-left")
# frm_left=driver.find_element_by_xpath("//body")
# print(frm_left.text)
#
# driver.switch_to.default_content()
# time.sleep(2)
# driver.switch_to.frame("frame-middle")
# frm_middle=driver.find_element_by_xpath("//div[@id='content']")
# print(frm_middle.text)
# driver.close()       dom is wrong




















#exa
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://testpages.eviltester.com/styled/iframes-test.html")
# driver.switch_to.frame('thedynamichtml')
# frame=driver.find_element_by_xpath("//iframe[@id='thedynamichtml']")
# print(frame.text)
# time.sleep(5)

#######################3practice
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://testpages.eviltester.com/styled/iframes-test.html")
# driver.maximize_window()
# driver.switch_to.frame('thedynamichtml')
# d=driver.find_element_by_xpath("//iframe[@id='thedynamichtml']")
# print(d.text)
# driver.close()                   #Unable to locate element: