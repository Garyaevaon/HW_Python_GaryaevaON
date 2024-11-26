from selenium import webdriver
from pages.MainPage_calculator import MainPage_calculator

def test_task_2():
    browser = webdriver.Chrome()

    main_page_calculator = MainPage_calculator(browser)
    main_page_calculator.enter_value("45")
    main_page_calculator.press_button_7()
    main_page_calculator.press_button_plus()
    main_page_calculator.press_button_8()
    main_page_calculator.press_button_rezult()
    main_page_calculator.waiter_resuit()
    result = main_page_calculator.result()
    assert result == "15"
    main_page_calculator.clouse_driver()
    

