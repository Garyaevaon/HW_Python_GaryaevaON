from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')

input.send_keys("1000")

sleep(3)

input.clear()

sleep(3)

input.send_keys("999")

sleep(3)

driver.quit()