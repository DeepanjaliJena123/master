# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# # driver.implicitly_wait(20)
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# # time.sleep(5)
# # alert=driver.find_element_by_xpath("//button[@onclick='jsAlert()']")
# # alert.click()
# # time.sleep(2)
# # obj1=driver.switch_to.alert
# # obj1.accept()
# # java_alert=driver.find_element_by_xpath("//button[@onclick='jsConfirm()']")
# # java_alert.click()
# # obj2=driver.switch_to.alert
# # obj2.dismiss()
# # time.sleep(2)
# js_alert=driver.find_element_by_xpath("//button[@onclick='jsPrompt()']")
# js_alert.click()
# obj3=driver.switch_to.alert
# obj3.send_keys("deepa")
# res=driver.find_element_by_xpath("//p[@id='result']")
# time.sleep(2)
#


#########popup

from selenium import webdriver
import time
driver=webdriver.Chrome()
# driver.implicitly_wait(20)
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
# time.sleep(5)
alertss=driver.find_element_by_xpath("//button[@id='promtButton']")
alertss.click()
obj=driver.switch_to.alert
obj.send_keys("python")
time.sleep(5)












