from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(20)

browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

src = browser.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")
print(src)

browser.quit()
