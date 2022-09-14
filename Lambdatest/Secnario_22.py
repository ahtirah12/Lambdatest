import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Browsers\chromedriver.exe")
driver.get("https://www.lambdatest.com/selenium-playground")
driver.find_element(By.PARTIAL_LINK_TEXT, "Drag & Drop Sliders").click()
#driver.find_element(By.CLASS_NAME, "sp__range").send_keys("15")
#driver.find_element(By.ID, "rangeSuccess").send_keys("95")
driver.find_element(By.CLASS_NAME, "sp__range").send_keys("95").click()
#driver.switch_to.drag(15,95)