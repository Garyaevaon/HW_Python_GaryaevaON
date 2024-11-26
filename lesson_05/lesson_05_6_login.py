from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

input_1 = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
input_1.send_keys("tomsmith")

input_2 = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
input_2.send_keys("SuperSecretPassword!")

input_3 = driver.find_element(By.CSS_SELECTOR, "button.radius").click()

sleep(3)

driver.quit()