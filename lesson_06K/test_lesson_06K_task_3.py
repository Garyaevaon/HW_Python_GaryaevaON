from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

def test_task3():
    browser.get("https://www.saucedemo.com/")

    Username = browser.find_element(
        By.CSS_SELECTOR, "#user-name")
    Username.clear()
    Username.send_keys("standard_user")

    Password = browser.find_element(
        By.CSS_SELECTOR, "#password")
    Password.clear()
    Password.send_keys("secret_sauce")

    browser.find_element(
        By.CSS_SELECTOR, "#login-button").click()
    browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    browser.find_element(
        By.CSS_SELECTOR, "#shopping_cart_container").click()
    browser.find_element(
        By.CSS_SELECTOR, "#checkout").click()

    FirstName = browser.find_element(
        By.CSS_SELECTOR, "#first-name")
    FirstName.clear()
    FirstName.send_keys("Ольга")

    LastName = browser.find_element(
        By.CSS_SELECTOR, "#last-name")
    LastName.clear()
    LastName.send_keys("Гаряева")

    PostalCode = browser.find_element(
        By.CSS_SELECTOR, "#postal-code")
    PostalCode.clear()
    PostalCode.send_keys("678188")

    browser.find_element(
        By.CSS_SELECTOR, "#continue").click()

    Total = browser.find_element(
        By.CSS_SELECTOR, "div.summary_total_label")
    txt = Total.text
    print(txt)

    assert "$58.29" in txt

    sleep(15)
    browser.quit()
