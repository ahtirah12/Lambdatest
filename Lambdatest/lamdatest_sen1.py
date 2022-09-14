
#**********SCENARIO 1 *************
from selenium import webdriver
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#driver = webdriver.Chrome(executable_path="C:/Users/mindtreefeb241/Downloads/chromedriver_win32/chromedriver.exe")
#driver = webdriver.Chrome(executable_path="C:\Browsers\chromedriver_win32 (3)\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Browsers\chromedriver.exe")

driver.get("https://www.lambdatest.com/selenium-playground")
time.sleep(3)
assert "Simple Form Demo" in "Simple Form Demo"
print("url is Validated")

driver.find_element(By.PARTIAL_LINK_TEXT,"Simple Form Demo").click()
time.sleep(5)


String="Welcome to lambdatest"
driver.find_element(By.ID,"user-message").send_keys(String)
driver.find_element(By.ID,"showInput").click()

#usr_msg=driver.find_element(By.ID,"user-message")
assert "Welcome to lambdatest" in String
time.sleep(2)
print("successfully checked")
driver.close()

