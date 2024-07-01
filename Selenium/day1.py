# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.selenium_manager import SeleniumManager
# driver=webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(2)
#
#
#
# # lnks=driver.find_elements_by_tag_name("a")
# # # traverse list
# # for lnk in lnks:
# #    # get_attribute() to get all href
# #    print(lnk.get_attribute("href"))
# # driver.quit()


# current_url=driver.current_url
# print(current_url)
# print(type(current_url))
# s="xyz"
# add_string=current_url+s
# print(add_string)
# driver.close()
#

# username=driver.find_element_by_xpath("//input[@name='username']")
# username.send_keys("Admin")
# password=driver.find_element_by_xpath("//input[@placeholder='Password']")
# password.send_keys("admin123")
# login=driver.find_element_by_xpath("//button[@type='submit']")
# login.click()
# admin=driver.find_element_by_xpath("//a[@href='/web/index.php/admin/viewAdminModule']")
# admin.click()
# add=driver.find_element_by_xpath("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
# add.click()
# pim=driver.find_element_by_xpath("//a[@href='/web/index.php/pim/viewPimModule']")
# pim.click()
# leave=driver.find_element_by_xpath("//a[@href='/web/index.php/leave/viewLeaveModule']")
# leave.click()
# time_t=driver.find_element_by_xpath("//a[@href='/web/index.php/time/viewTimeModule']")
# time_t.click()
# recruitment=driver.find_element_by_xpath("//a[@href='/web/index.php/recruitment/viewRecruitmentModule']")
# recruitment.click()
# myinfos=driver.find_element_by_xpath("//a[@href='/web/index.php/pim/viewMyDetails']")
# myinfos.click()
# performance=driver.find_element_by_xpath("//a[@href='/web/index.php/performance/viewPerformanceModule']")
# performance.click()
# dashboard=driver.find_element_by_xpath("//a[@href='/web/index.php/dashboard/index']")
# dashboard.click()
# directory=driver.find_element_by_xpath("//a[@href='/web/index.php/directory/viewDirectory']")
# directory.click()
# # maintenance=driver.find_element_by_xpath("//a[@href='/web/index.php/maintenance/viewMaintenanceModule']")
# # maintenance.click()
# claim=driver.find_element_by_xpath("//a[@href='/web/index.php/claim/viewClaimModule']")
# claim.click()
# buz=driver.find_element_by_xpath("//a[@href='/web/index.php/buzz/viewBuzz']")
# buz.click()

# userole=driver.find_element_by_xpath("(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
# userole.click()
# # employeename=driver.find_element_by_xpath("(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
# # employeename.click()
# empname=driver.find_element_by_xpath("//input[@placeholder='Type for hints...']")
# empname.send_keys("Deepanjali Jena")
# usernames=driver.find_element_by_xpath("(//input[@class='oxd-input oxd-input--active'])[2]")
# usernames.send_keys("deep")
# pssworrd=driver.find_element_by_xpath("(//input[@type='password'])[1]")
# pssworrd.send_keys("deep@123")
# conformpassword=driver.find_element_by_xpath("(//input[@type='password'])[2]")
# conformpassword.send_keys("deep@123")
# time.sleep(5)



print("hello welcome")




