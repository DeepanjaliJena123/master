from selenium.webdriver import Chrome
import time
driver=Chrome()
driver.maximize_window()
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
# driver.implicitly_wait(30)
car=driver.find_element_by_xpath("//input[@value='Car']")
bike=driver.find_element_by_xpath("//input[@value='Bike']")
driver.execute_script("arguments[0].scrollIntoView();",bike)
bike.click()
time.sleep(2)car.click()

print(car.is_selected()) #validate car is select or not

# for looping
# x=driver.find_elements_by_xpath("//input[@type='checkbox']")
# for i in range(len(x)):
#     x[i].click()

#checking selected or not
# if bike.is_selected():
#     bike.click()
#     print("bike selected")
# else:
#     bike.click()
#     print("not selected")

#check select or not
x=driver.find_elements_by_xpath("//input[@type='checkbox']")
for i in range(len(x)):
    if x[i].is_selected()==False:
        x[i].click()
    print(x[i].text,"is",x[i].is_selected())
driver.close()