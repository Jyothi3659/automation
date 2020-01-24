from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.gcrit.com/build3/")
driver.find_element_by_link_text("login").click()
driver.find_element_by_name("email_address").send_keys("asdfghj@gmail.com")
driver.find_element_by_name("password").send_keys("abcd123")
driver.find_element_by_xpath("//*[@id='tdb5']/span[2]").click()
try :
    if (driver.find_element_by_link_text("Log Off")).is_displayed():
        print("success")
except NoSuchElementException :
    print("failed")

time.sleep(2)
driver.close()
driver.quit()
print("test done")
