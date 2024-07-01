from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time
driver=Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
element=driver.find_element_by_id("dropdown")
# obj=Select(element)
# obj.select_by_value("1")
# time.sleep(5)
# obj.select_by_index(2)
# time.sleep(5)
# obj.select_by_visible_text("Option 1")
# time.sleep(2)

## #all values find
# value=obj.options
# for i in range(len(value)):
#     s=value[i]
#     txt=s.text
#     print(txt)

#or ### Get all available element options from dropdown list:
# obj=Select(element)
# all_dropdwonOptions=obj.options
# for i in range (len(all_dropdwonOptions)):
#     option=all_dropdwonOptions[i]
#     text=option.text
#     print(text)
# driver.close()


### Select a particular option from dropdown list
# obj=Select(element)
# all_dropdwonOptions=obj.options
#
# for i in range(len(all_dropdwonOptions)):
#     option=all_dropdwonOptions[i]
#     text=option.text
#     if text=="Option 1":
#         obj.select_by_index(i)
#         break
# driver.close()


###### Select the last option from dropdown list
# obj=Select(element)
# all_dropdwonOptions=obj.options
# size=len(all_dropdwonOptions)
# last_option=obj.select_by_index(size-1)           #doubt


######## Get selected option from dropdown
# obj=Select(element)
# obj.select_by_index(2)
# selected_opt=obj.all_selected_options
# for i in range(len(selected_opt)):
#     opt=selected_opt[i]
#     txt=opt.text
#     print(txt)
# driver.close()

##### select multiple option from dropdwon
# obj=Select(element)
# selected_opt=obj.all_selected_options
# for i in range(0,len(selected_opt)):
#     options=selected_opt[i]
#     txt=options.text
#     print(txt)
# driver.close()

##### Deselect an option from dropdown
#Dselect is only allowed on multi select dropdown list and we cant not use these
#deselect options in sinlge single select dropdown list
# obj=Select(element)
# obj.select_by_index(2)
# time.sleep(5)
# obj.deselect_by_index()
# obj.deselect_all()
# obj.deselect_by_value()
# obj.deselect_by_visible_text()
#

####### Check a dropdwon is single select or multiselect
# obj=Select(element)
# status=obj.is_multiple
# if status==True:
#     print("yes, multiple")
# else:
#     print("no")








##### Execptions ###
#1.Stable Element Reference Exception
#if element is identified before refresh or reload and action is performed after refresh or reload
#selenium will throw stable element referrence exception

#2.