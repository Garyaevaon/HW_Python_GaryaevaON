from selenium import webdriver
from pages.MainPage_saucedemo import MainPage_saucedemo

def test_task_3():
    browser = webdriver.Chrome()

    main_page_saucedemo = MainPage_saucedemo(browser)
    main_page_saucedemo.enter_username("standard_user")
    main_page_saucedemo.enter_password("secret_sauce")
    main_page_saucedemo.login()
    main_page_saucedemo.add_element_1()
    main_page_saucedemo.add_element_2()
    main_page_saucedemo.add_element_3()
    main_page_saucedemo.shopping_cart_container()
    main_page_saucedemo.checkout()
    main_page_saucedemo.enter_first_name("Ольга")
    main_page_saucedemo.enter_last_name("Гаряева")
    main_page_saucedemo.enter_postal_code("678188")
    main_page_saucedemo.enter_continue()
    result = main_page_saucedemo.enter_total_label()
    assert result == "Total: $58.29"
    main_page_saucedemo.clouse_driver()

