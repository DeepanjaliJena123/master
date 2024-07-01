# #exa1
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
# # plagroundclick1=driver.find_element_by_xpath("//a[@title='Active Link']")
# # mouse.double_click(plagroundclick1).perform()
#
# mouse.context_click(plagroundclick).perform()


##############################practice
from selenium.webdriver import Chrome,ActionChains
import time
driver=Chrome()
driver.get("http://www.uitestingplayground.com/mouseover")
driver.maximize_window()
p=driver.find_element_by_xpath("//a[@title='Click me']")
mouse=ActionChains(driver=driver)
mouse.move_to_element(p).perform()
time.sleep(5)
driver.close()

#for left menu click
# mouse.context_click(p).perform()       #for left click
# time.sleep(5)
# driver.close()















# #exa2
# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.maximize_window()
# driver.get("https://www.globalsqa.com/demo-site/draganddrop/#Photo%20Manage")
# driver.implicitly_wait(30)
# driver.switch_to.frame('google_esf')
# time.sleep(8)
# source=driver.find_element_by_xpath("(//li[@class='ui-widget-content ui-corner-tr ui-draggable ui-draggable-handle'])[1]")
# target=driver.find_element_by_xpath("//div[@id='trash']")
# # globalsqa=driver.find_element_by_xpath("(//li[@role='tab'])[1]")
# mouse=ActionChains(driver=driver)
# time.sleep(2)
# mouse.move_to_element(source).click_and_hold().move_to_element(target).release().perform()
# time.sleep(5)
# # not worked, website probelem


##exa
# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.get("https://the-internet.herokuapp.com/hovers")
# driver.implicitly_wait(30)
# user1=driver.find_element_by_xpath("(//img[@alt='User Avatar'])[1]")
# mouse=ActionChains(driver=driver)
# mouse.move_to_element(user1).perform()
# time.sleep(2)
# user1veiw=driver.find_element_by_xpath("//a[@href='/users/1']")
# mouse.click(user1veiw).perform()
# time.sleep(5)
# print(user1veiw.text)
# time.sleep(2)


#exa
# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.maximize_window()
# driver.implicitly_wait(30)
# driver.get("https://letcode.in/dropable")
# time.sleep(2)
# mouse=ActionChains(driver=driver)
# source=driver.find_element_by_xpath("//div[@id='draggable']")
# target=driver.find_element_by_xpath("//div[@id='droppable']")
# mouse.move_to_element(source).click_and_hold().move_to_element(target).release().perform()
# time.sleep(5)
# print(target.text)
# time.sleep(5)

##exa normal op
# from selenium.webdriver import Chrome
# import time
# driver=Chrome()
# driver.implicitly_wait(30)
# driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
# time.sleep(2)
# for i in range(5):
#     element=driver.find_element_by_xpath("//button[@onclick='addElement()']")
#     element.click()
#     time.sleep(3)
# for i in range(5):
#     delete = driver.find_element_by_xpath("//button[@onclick='deleteElement()']")
#     delete.click()
#     time.sleep(3)










