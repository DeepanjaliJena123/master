from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(60)
driver.get("https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP")
driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(5)
# driver.refresh()
# time.sleep(5)
# title=driver.title
# print(title)
# url=driver.current_url
# print(url)
# s="xyz"
# add=url+s
# print(add)
# driver.close()

# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(60)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
# time.sleep(5)
# size=driver.get_window_size()
# print(size)
# print(size['height'])
# print(size['width'])
# driver.close()


# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(60)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
# time.sleep(5)
# # cookies=driver.get_cookies()
# # print(cookies)
# cookie_data={"secure":False,"domain":"google.com"}
# driver.add_cookie(cookie_data)
# print(driver.get_cookies())
# time.sleep(5)

# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(60)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(5)
# user=driver.find_element_by_xpath("//input[@placeholder='Username']")
# user.send_keys("Admin")
# time.sleep(2)
# # password=driver.find_element_by_xpath("//input[@placeholder='Password']")
# # password.send_keys("admin123")
# # login=driver.find_element_by_xpath("//button[@type='submit']")
# # login.click()
# # time.sleep(5)

#####  get size of a textbox  ##########

# from selenium import webdriver
# import time
# driver=webdriver.Chrome
# driver.implicitly_wait()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# size_textbox=driver.find_element_by_name("username")
# size=size_textbox.size
# print(size)
# print(size["height"])
# print(size["width"])
# time.sleep(2)
# driver.close()



###### Verify the size of two textboxes #######3
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(60)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(5)
# user=driver.find_element_by_xpath("//input[@placeholder='Username']")
# user.send_keys("Admin")
# user_size=user.size
# time.sleep(2)
# password=driver.find_element_by_xpath("//input[@placeholder='Password']")
# password.send_keys("admin123")
# password_size=password.size
# # login=driver.find_element_by_xpath("//button[@type='submit']")
# # login.click()
# if user_size["height"]==password_size["height"] and user_size["width"]==password_size["width"]:
#     print("passed")
# else:
#     print("faild")
# time.sleep(5)
# driver.close()

####### get the position of textbox on a webpage ######

# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(60)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(5)
# user_textbox=driver.find_element_by_xpath("//input[@placeholder='Username']")
# position=user_textbox.location
# print(position)
# print("x",position["x"])
# print("y",position["y"])
# time.sleep(2)
# driver.close()

##########   mouase operation   #########
# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.get("http://www.uitestingplayground.com/mouseover")
# driver.implicitly_wait(60)
# click_playground=driver.find_element_by_class_name("text-primary")
# mouse=ActionChains(driver=driver)
# mouse.move_to_element(click_playground).perform()
# time.sleep(5)
# mouse.double_click(click_playground).perform()
# time.sleep(5)
# driver.close()

####### drag n drop ##########
# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.get("https://www.globalsqa.com/demo-site/draganddrop/#Photo%20Manage")
# driver.implicitly_wait(60)
# source=driver.find_element_by_xpath("(//li[@class='ui-widget-content ui-corner-tr ui-draggable ui-draggable-handle'])[1]")
# target=driver.find_element_by_id('trash')
# mouse=ActionChains(driver=driver)
# mouse.move_to_element(source).click_and_hold().move_to_element(target).release().perform()
# time.sleep(5)
# driver.close()

### mouse operation ###
# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome
# driver.get("https://the-internet.herokuapp.com/hovers")
# driver.implicitly_wait(60)
# user1=driver.find_element_by_xpath("(//div[@class='figure'])[1]")
# user_view=driver.find_element_by_xpath("//a[@href='/users/1']")
# mouse=ActionChains(driver=driver)
# mouse.move_to_element(user1).perform()
# time.sleep(3)
# mouse.click(user_view).perform()
# time.sleep(5)  ## error

########### drag n drop #####
# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.implicitly_wait(60)
# driver.get("https://letcode.in/dropable")
# time.sleep(5)
# source=driver.find_element_by_id('draggable')
# target=driver.find_element_by_id('droppable')
# mouse=ActionChains(driver=driver)
# mouse.move_to_element(source).click_and_hold().move_to_element(target).release().perform()
# time.sleep(5)
# print(target.text)
# time.sleep(5)       ####error


#######  operation  #####
# from selenium.webdriver import Chrome
# import time
# driver=Chrome()
# driver.implicitly_wait(30)
# driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
# for i in range(5):
#     element=driver.find_element_by_xpath("//button[@onclick='addElement()']")
#     element.click()
#     time.sleep(5)
# for i in range(5):
#     delete=driver.find_element_by_xpath("//button[@class='added-manually']")
#     delete.click()
#     time.sleep(5)
# driver.close()

##### drag n drop #########
# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.implicitly_wait(30)
# A=driver.find_element_by_xpath("//div[@id='column-a']")
# B=driver.find_element_by_xpath("//div[@id='column-b']")
# mouse=ActionChains(driver=driver)
# mouse.move_to_element(A).click_and_hold().move_to_element(B).release().perform()
# time.sleep(5)
# driver.close()
















