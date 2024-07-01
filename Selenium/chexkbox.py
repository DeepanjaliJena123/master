# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.maximize_window()
# driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
# # time.sleep(5)
# driver.implicitly_wait(60)
# female_click=driver.find_element_by_xpath("//input[@value='female']")
# # mouse=ActionChains(driver=driver)
# # mouse.move_to_element(female_click).click().perform()
# #or
# #using js to scroll
# driver.execute_script("arguments[0].scrollIntoView();", female_click)
# female_click.click()
# time.sleep(5)
# #exa

# from selenium.webdriver import Chrome
# import time
# driver=Chrome()
# driver.maximize_window()
# driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
# driver.implicitly_wait(30)
# bike=driver.find_element_by_xpath("//input[@value='Bike']")
# car=driver.find_element_by_xpath("//input[@value='Car']")
# driver.execute_script("arguments[0].scrollIntoView();",bike)
# bike.click()
# car.click()
# print(car.is_selected())      #for validation
# time.sleep(5)

# for looping
# x=driver.find_elements_by_xpath("//input[@type='checkbox']")
# for i in range(len(x)):
#     x[i].click()

# y=driver.find_elements("//input[@type='radio']")
# for i in range(len(y)):
#     y[i].click()



# bike=driver.find_element_by_xpath("//input[@value='Bike']")
# bike.click()
# time.sleep(5)
# driver.execute_script("arguments[0].scrollIntoView();",bike)
# if bike.is_selected():
#     bike.click()
#     print("bike is select")
# else:
#     bike.click()
#     print("not selected")
#     time.sleep(5)

#
# car=driver.find_element_by_xpath("//input[@value='Car']")
# bike=driver.find_element_by_xpath("//input[@value='Bike']")
# bike.click()
# time.sleep(5)
# x=driver.find_elements_by_xpath("//input[@type='checkbox']")
# driver.execute_script("arguments[0].scrollIntoView();",bike)
# time.sleep(5)
# for i in range(len(x)):
#
#     if x[i].is_selected()==False:
#         x[i].click()
#     print(x[i].text,"is",x[i].is_selected())
# driver.close()
#
