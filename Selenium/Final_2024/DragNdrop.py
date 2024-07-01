from selenium.webdriver import Chrome,ActionChains
import time
driver=Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.implicitly_wait(30)
source=driver.find_element_by_id('column-a')
Target=driver.find_element_by_id("column-b")
d=ActionChains(driver=driver)
# d.move_to_element(source).click_and_hold().move_to_element(Target).release().perform()
#or
d.drag_and_drop(source,Target).perform()
time.sleep(5)