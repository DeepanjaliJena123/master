# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# #only click
# js=driver.find_element_by_xpath("//button[@onclick='jsAlert()']")
# js.click()
# time.sleep(5)

#click n accecpt n cancel or dismis
# js_confm=driver.find_element_by_xpath("//button[@onclick='jsPrompt()']")
# js_confm.click()
# time.sleep(2)
# obj=driver.switch_to.alert
# # time.sleep(2)
# # obj.accept()
# obj.dismiss()
# time.sleep(2)
# driver.close()

#### get msg available on peg
# msg=obj.text
# print(msg)
# obj.accept()

##### enter value n validate
# js_prompt=driver.find_element_by_xpath("//button[@onclick='jsPrompt()']")
# js_prompt.click()
# obj=driver.switch_to.alert
# obj.send_keys("i am jen")
# obj.accept()
# time.sleep(2)
# res=driver.find_element_by_xpath("//p[@id='result']")
# visible_element=res.text
# if visible_element=="You entered: i am jen":
#     print("valid")
# else:
#     print("not valid")
#

#interview qstn
####### Network Aunthentication PopUp:::
#this popup is designed using Javascript and
#we can not handle this popup using Selenium.

### Non Inspectable Components::
#-But we can bypass this popup by modifying the current URL
#current_url= http://www.info.com/login.ht ml
#Modified_url="http://Admin123:Pass123@www.infor.com/login.html"
#driver.get(modified_url)


### Hidden Divivsion Popup
from selenium import webdriver
import time
driver=webdriver.Chrome()
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver.get("https://www.yatra.com/")
driver.maximize_window()
driver.find_element_by_id('BE_flight_origin_date').click()
date=driver.find_element_by_id("13/04/2024")
wait=WebDriverWait(driver=driver,timeout=30)
wait.until(expected_conditions.visibility_of(date))
date.click()







