from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://uitestingplayground.com/dynamicid")

sleep(1)

driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']").click()

sleep(3)

driver.quit()