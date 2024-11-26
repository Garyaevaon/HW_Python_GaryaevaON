from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://uitestingplayground.com/textinput")

element = browser.find_element(By.CSS_SELECTOR, "#newButtonName")
element.clear()
element.send_keys("Skypro")

browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()

txt = browser.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(txt)

browser.quit()
