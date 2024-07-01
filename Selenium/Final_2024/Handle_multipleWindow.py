from PIL import Image
from selenium.webdriver import Chrome
import time
from PIL import Image
# driver=Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")
# driver.maximize_window()
# child_window=driver.find_element_by_link_text("Click Here")
# child_window.click()
# time.sleep(2)
# all_windows=driver.window_handles
# parent=all_windows[0]
# child=all_windows[1]
# driver.switch_to.window(parent)
# print(driver.title)
# time.sleep(2)
# driver.switch_to.window(child)
# print(driver.title)
# time.sleep(5)
#
# #### Screenshot
# driver.save_screenshot("abc.png")
im = Image.open("abc.png")
im.show()