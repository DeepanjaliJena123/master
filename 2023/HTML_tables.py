from selenium.webdriver import Chrome
import time
driver=Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()
time.sleep(2)
driver.get_screenshot_as_file("srcn.jpg")
time.sleep(2)
# loc_germany=driver.find_element_by_xpath("//table//tbody//tr//td[contains(text(),'Germany')]")
#or u can take tr and td row column wise
# loc_germany=driver.find_element_by_xpath("//table[@class='ws-table-all']/tbody/tr[2]/td[3]")
# comp_name=driver.find_element_by_xpath("//table[@class='ws-table-all']/tbody/tr[5]/td[1]")
#
# print(comp_name.text)
# time.sleep(2)
driver.close()