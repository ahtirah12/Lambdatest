
#************SCENARIO 3 ************

from selenium import webdriver
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import unittest

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\Browsers\chromedriver.exe")
        driver.get("https://www.lambdatest.com/selenium-playground")
        driver.maximize_window()
        print("website opened correctly")
        time.sleep(2)
        # driver.find_element(By.CLASS_NAME,"inline-block").click()
        driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
        driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
        # driver.find_element(By.XPATH,"//*[@id="seleniumform"]/div[6]/button").perform()
        alt = driver.find_element(By.CSS_SELECTOR, "#seleniumform > div.text-right.mt-20 > button").click()
        assert "Please fill out this field" in "Please fill out this field"
        print("Please fill out this field")

        driver.find_element(By.ID, "name").send_keys("haritha")
        time.sleep(2)
        driver.find_element(By.ID, "inputEmail4").send_keys("parnaplliharitha0@gmail.com")
        driver.find_element(By.ID, "inputPassword4").send_keys("123456")
        driver.find_element(By.NAME, "company").send_keys("xyzabc")
        driver.find_element(By.NAME, "website").send_keys("Lambdatest.com")
        # driver.find_element(By.NAME,"country").send_keys("#seleniumform > div:nth-child(3) > div.form-group.w-6\/12.smtablet\:w-full.pr-20.smtablet\:pr-0 > select > option:nth-child(104)").perform()
        driver.find_element(By.NAME, "country").send_keys("IN")
        driver.find_element(By.ID, "inputCity").send_keys("Atp")
        driver.find_element(By.NAME, "address_line1").send_keys("Ananthapur")
        driver.find_element(By.ID, "inputAddress2").send_keys("Singanamala")
        driver.find_element(By.ID, "inputState").send_keys("AP")
        driver.find_element(By.ID, "inputZip").send_keys("515435")
        time.sleep(5)
        # driver.find_element(By.XPATH,"//*[@id="inputZip"]").send_keys("515435")
        # driver.find_element(By.XPATH,"//*[@id="seleniumform"]/div[6]/button").click()
        # driver.find_element(By.CLASS_NAME,"btn btn-dark selenium_btn bg-black text-white hover:bg-lambda-900 py-5 px-10 rounded").click()
        driver.find_element(By.CSS_SELECTOR, "#seleniumform > div.text-right.mt-20 > button").click()

        # sub_text=sub.text
        assert "Thanks for contacting us, we will get back to you shortly" in "Thanks for contacting us, we will get back to you shortly"
        time.sleep(5)
        print("Successfully submitted")
        driver.close()


tt=Test()
tt.testName()


