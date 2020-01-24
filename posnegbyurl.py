from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="drivers/chromedriver")
driver.get("http://www.gcrit.com/build3/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin@123")
driver.find_element_by_xpath("//*[@id='tdb1']/span[2]").click()
cur_url = driver.current_url
if cur_url == "http://www.gcrit.com/build3/admin/index.php":
    print("sucess")
time.sleep(2)
driver.close()
