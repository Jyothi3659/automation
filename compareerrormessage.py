from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="drivers/chromedriver")
driver.get("http://www.gcrit.com/build3/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='tdb1']/span[2]").click()
cur_url = driver.current_url
error_message = "None"
if cur_url != "http://www.gcrit.com/build3/admin/index.php":
    error_message = driver.find_element_by_class_name("messageStackError").text
    print(error_message)
if cur_url == "http://www.gcrit.com/build3/admin/index.php":
    print("sucess")
elif (cur_url != "http://www.gcrit.com/build3/admin/index.php") and (error_message.__contains__("Invalid administrator login attempt.")):
    print("login faild and correct error message")
else :
    print("login faild nd error failed")
time.sleep(2)
driver.close()
driver.quit()