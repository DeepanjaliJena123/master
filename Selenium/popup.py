# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# # time.sleep(5)
# # driver.maximize_window()
# driver.implicitly_wait(60)
# # # alerts=driver.find_element_by_xpath("//button[@onclick='jsAlert()']")
# # # alerts.click()
# # # time.sleep(5)
# # # alerts=driver.find_element_by_xpath("//button[@onclick='jsConfirm()']")
# # # alerts.click()
# alerts=driver.find_element_by_xpath("//button[@onclick='jsPrompt()']")
# alerts.click()
# obj=driver.switch_to.alert
# obj.send_keys("deepa")

# # # obj.accept()
# # # obj.dismiss()
# obj.accept()
# result=driver.find_element_by_xpath("//p[@id='result']")
# time.sleep(2)
# val=result.text
# if val == "You entered: peepa":
#     print("tc pass")
# else:
#     print("tc fail")
# driver.close()


##########practice
#start
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(5)
# driver.maximize_window()
#alrt1
# alerts=driver.find_element_by_xpath("//button[@onclick='jsAlert()']")
# alerts.click()
# time.sleep(2)
# obj=driver.switch_to.alert
# #alert text validation
# res=obj.text
# if res=="I am a JS Alert":
#     print("yes")
# else:
#     print("no")
# obj.accept()
# driver.close()

#alrt2
# alrt2=driver.find_element_by_xpath("//button[@onclick='jsPrompt()']")
# alrt2.click()
# obj1=driver.switch_to.alert
# obj1.send_keys("deep")
# obj1.accept()
# driver.close()
#close
#################################################


#
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(30)
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# # first_alert=driver.find_element_by_xpath("//button[@onclick='jsAlert()']")
# # first_alert.click()
# # time.sleep(5)
# # driver.close()
# # second_alert=driver.find_element_by_xpath("//button[@onclick='jsConfirm()']")
# # second_alert.click()
# # time.sleep(2)
#
# third_alert=driver.find_element_by_xpath("//button[@onclick='jsPrompt()']")
# third_alert.click()
# time.sleep(2)
# obj=driver.switch_to.alert
# obj.send_keys("deep")
# obj.accept()     ##for accept,ok deepa will show in result
# obj.dismiss()    ##for dismiss, resulit will nul










