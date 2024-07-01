# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.implicitly_wait(30)
# source=driver.find_element_by_xpath("(//div[@draggable='true'])[1]")
# target=driver.find_element_by_xpath("(//div[@draggable='true'])[2]")
# drd=ActionChains(driver=driver)
# # time.sleep(5)
# drd.move_to_element(source).click_and_hold().move_to_element(target).release().perform()
# time.sleep(5)
# drd.move_to_element(target).click_and_hold().move_to_element(source).release().perform()
# # or
# drd.drag_and_drop(source,target).perform()
# time.sleep(5)
# drd.drag_and_drop(source,target).perform()

########prac
# from selenium.webdriver import Chrome, ActionChains
# import time
# driver=Chrome()
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.maximize_window()
# source=driver.find_element_by_xpath("(//div[@class='column'])[1]")
# Target=driver.find_element_by_xpath("(//div[@class='column'])[2]")
# obj=ActionChains(driver=driver)
# obj.move_to_element(source).click_and_hold().move_to_element(source).release().perform()
# # obj.drag_and_drop(source,Target).perform()
# time.sleep(5)
# driver.close()
########################


#exa
# from selenium.webdriver import Chrome,ActionChains
# import time
# driver=Chrome()
# driver.get("https://testpages.eviltester.com/styled/drag-drop-javascript.html")
# driver.implicitly_wait(30)
# source=driver.find_element_by_xpath("//div[@id='draggable1']")
# target=driver.find_element_by_xpath("//div[@id='droppable1']")
# d=ActionChains(driver=driver)
# time.sleep(2)
# # d.move_to_element(source).click_and_drag.move_to_element(target).release.perform()
# d.drag_and_drop(source,target).perform()
# print(target.text)
# time.sleep(5)
# source1=driver.find_element_by_xpath("//div[@id='draggable2']")
# target1=driver.find_element_by_xpath("//div[@id='droppable2']")
# d1=ActionChains(driver=driver)
# time.sleep(2)
# d1.drag_and_drop(source1,target1).perform()
# print(target1.text)
# time.sleep(5)
