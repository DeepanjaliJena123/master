# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(30)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# title_print=driver.title
# print(title_print)
# current_url=driver.current_url
# print(current_url)
# s="xyz123"
# add=current_url+s
# print(add)
# driver.close()

# user_name=driver.find_element_by_xpath("//input[@placeholder='Username']")
# user_name.send_keys("Admin")
# password=driver.find_element_by_xpath("//input[@type='password']")
# password.send_keys("admin123")
# login=driver.find_element_by_xpath("//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
# login.click()

###   Normal Operation   ###
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(30)
# driver.get("https://opensource")
# time.sleep(3)
# driver.back()
# driver.forward()
# title_print=driver.title
# print(title_print)
# current_url=driver.current_url
# print(current_url)
# s="xyz123"
# add=current_url+s
# print(add)
# driver.close()
############################

###### Mouse Operation ############

# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.get("http://www.uitestingplayground.com/mouseover")
# driver.implicitly_wait(30)
# plagroundclick=driver.find_element_by_xpath("//a[@title='Click me']")
# mouse=ActionChains(driver=driver)
# # mouse.move_to_element(plagroundclick).perform()
# time.sleep(5)
# # mouse.click(plagroundclick).perform()
# # time.sleep(5)
# plagroundclick1=driver.find_element_by_xpath("//a[@title='Active Link']")
# mouse.double_click(plagroundclick1).perform()
#
# # mouse.context_click(plagroundclick).perform()        #for right click
# time.sleep(3)
# driver.close()


#######mouse operation #######
# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.get("http://www.uitestingplayground.com/mouseover")
# driver.implicitly_wait(60)
# click_playground=driver.find_element_by_xpath("//a[@title='Click me']")
# mouse=ActionChains(driver=driver)
# mouse.move_to_element(click_playground).perform()
# time.sleep(5)
# mouse.double_click(click_playground).perform()
# time.sleep(5)
# driver.close()

### multiple window #######
from selenium import webdriver
import time
from PIL import Image
driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://the-internet.herokuapp.com/windows")
window=driver.find_element_by_xpath("//a[@href='/windows/new']")
window.click()
time.sleep(3)









