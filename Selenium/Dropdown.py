# from selenium.webdriver import Chrome
# from selenium.webdriver.support.select import Select
# import time
# driver=Chrome()
# driver.get("https://the-internet.herokuapp.com/dropdown")
# driver.implicitly_wait(30)
# dropdown=driver.find_element_by_xpath("//select[@id='dropdown']")
# obj=Select(dropdown)
# obj.select_by_value('1')
# time.sleep(3)
# obj.select_by_index(2)
# time.sleep(3)
# obj.select_by_visible_text("Option 1")
# #all values find
# obj1=Select(dropdown)
# val=obj1.options
# for i in range(len(val)):
#     s=val[i]
#     d=s.text
#     print(d)
# find last value
# obj1=Select(dropdown)
# val=obj1.options
# print(len(val))
# t=val[len(val)-1]
# obj1.select_by_visible_text(t.text)
# time.sleep(3)
#
# obj1.deselect_by_visible_text(t.text)
#
# import time


#############practice
# from selenium.webdriver import Chrome
# from selenium.webdriver.support.select import Select
# import time
# driver=Chrome()
# driver.get("https://the-internet.herokuapp.com/dropdown")
# driver.maximize_window()
# # drp_dwn=driver.find_element_by_xpath("//select[@id='dropdown']")
# # obj=Select(drp_dwn)
# #print textOption 1
# # k=driver.find_element_by_xpath("//option[@value='1']")
# # print(k.text)
# # # obj.select_by_index(2)
# # # obj.select_by_visible_text("Option 1")
#
# #print all dropdown options
# #1st identify location of element
# drp_dwn=driver.find_element_by_xpath("//select[@id='dropdown']")
# obj=Select(drp_dwn)
# opt=obj.options
#
# for i in range(len(opt)):
#     s=opt[i]
#     v=s.text
#     print(v)
# driver.close()



# ## new web application
#
# from selenium.webdriver import Chrome
# from selenium.webdriver.support.select import Select
# import time
# driver=Chrome()
# driver.get("https://www.saucedemo.com/inventory.html")
# driver.implicitly_wait(30)
# # dropdown1=driver.find_element_by_xpath("//select[@data-test='product_sort_container']")
# user_s=driver.find_element_by_xpath("//input[@placeholder='Username']")
# user_s.send_keys("standard_user")
# paswrd=driver.find_element_by_xpath("//input[@placeholder='Password']")
# paswrd.send_keys("secret_sauce")
# loginn=driver.find_element_by_xpath("//input[@data-test='login-button']")
# loginn.click()
# time.sleep(2)
# dropdown=driver.find_element_by_xpath("//select[@data-test='product_sort_container']")
# obj=Select(dropdown)
# # obj.select_by_value('lohi')
# time.sleep(2)
# # obj.select_by_index(1)
# # obj.select_by_visible_text('Z to A')
# # time.sleep(2)
# val=obj.options
# for i in range(len(val)):
#     a=val[i]
#     k=a.text
#     print(k)

###########
#
# from selenium.webdriver import Chrome
# from selenium.webdriver.support.select import Select
# import time
# driver=Chrome()
# driver.get("https://the-internet.herokuapp.com/dropdown")
# driver.implicitly_wait(30)
# dropNdown=driver.find_element_by_id('dropdown')
# dropNdown.click()
# time.sleep(2)
# obj=Select(dropNdown)
# obj.select_by_value(1)
# time.sleep(2)
# obj.select_by_index(2)
# time.sleep(2)
# obj.select_by_visible_text("Option 1")
#

