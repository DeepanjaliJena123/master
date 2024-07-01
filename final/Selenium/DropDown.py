#Dropdown
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time
driver=Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.implicitly_wait(30)
element_drpdwn=driver.find_element_by_xpath("//select[@id='dropdown']")
time.sleep(3)