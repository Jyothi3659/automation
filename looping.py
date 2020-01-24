from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="drivers/chromedriver")
error_message = "None"
username = "None"
password = "None"
iteration = 0
error = None
driver.get("http://www.gcrit.com/build3/admin/")
for each in range(1,2):
    if each == 1:
        username = "admin"
        password = "admin123"
        iteration = 1
        error = "Invalid administrator login attempt."
    elif each == 2:
        username = " "
        password = "admin"
        iteration = 2
        error = "Invalid administrator login atempt."

driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_xpath("//*[@id='tdb1']/span[2]").click()
cur_url = driver.current_url

if cur_url != "http://www.gcrit.com/build3/admin/index.php":
    error_message = driver.find_element_by_class_name("messageStackError").text
    print(error_message)
if cur_url == "http://www.gcrit.com/build3/admin/index.php":
    print("Iteration " + str(iteration) + "sucess")
elif (cur_url != "http://www.gcrit.com/build3/admin/index.php") and (error_message.__contains__(error)):
    print("iteration" + str(iteration) + "login faild and correct error message")
else :
    print("login faild nd error failed")
time.sleep(2)
driver.close()
driver.quit()