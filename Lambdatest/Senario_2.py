from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DemoDragDrop():
    def drag_drop(self):
        driver = webdriver.Chrome(executable_path="C:\Browsers\chromedriver.exe")
        driver.get("https://www.lambdatest.com/selenium-playground")
        driver.find_element(By.PARTIAL_LINK_TEXT, "Drag & Drop Sliders").click()
        #driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/div[1]/div/section[3]/div/div/div[2]/div[2]/div[1]/div/input"))
        #driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id="slider3"]/div/input"))
        #elem1=driver.find_element(By.XPATH,"rangeSuccess")
        #elem2=driver.find_element(By.XPATH,"rangeSuccess")

        #action = ActionChains(driver)
        #action.click_and_hold(min1).move_by_offset(15, 95).pause(2).move_by_offset(-10, -10).release().perform()
        #action.drag_and_drop("15","95").perform()
        driver.find_element(By.CLASS_NAME,"sp__range sp__range-success").send_keys("95")
        #driver.find_element(By.ID,"rangeSuccess").send_keys("95")
        #ActionChains(driver).drag_and_drop(elem1,elem2).perform()

        #source_element = driver.find_element(By.XPATH,("//*[@id="slider3"]/div/15"))
        #target_element = driver.find_element(By.XPATH,("//*[@id="slider3"]/div/95"))
        #actions = ActionChains(driver)
        #actions.drag_and_drop(source_element, target_element).perform()


dd=DemoDragDrop()
dd.drag_drop()


#driver.maximize_window()
#time.sleep(3)
#driver.find_element(By.CLASS_NAME,"st_heading").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Drag & Drop Sliders").click()
#driver.find_element(By.CLASS_NAME,"sp__range").send_keys("95").drag()