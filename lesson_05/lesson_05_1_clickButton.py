from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    AddElement = driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

sleep(3)

RemoveElement = driver.find_elements(By.XPATH, "//button[text()='Delete']")
print(len (RemoveElement))

driver.quit()