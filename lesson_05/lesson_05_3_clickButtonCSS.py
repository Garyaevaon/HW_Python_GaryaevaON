from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

sleep(3)

driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

sleep(3)

driver.quit()