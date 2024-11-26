from selenium import webdriver
from pages.MainPage_datatypes import MainPage_bonigarcia

def test_task_1():
    browser = webdriver.Chrome()

    main_page_bonigarcia = MainPage_bonigarcia(browser)
    main_page_bonigarcia.add_first_name("Иван")
    main_page_bonigarcia.add_last_name("Петров")
    main_page_bonigarcia.add_address("Ленина, 55-3")
    main_page_bonigarcia.add_email("test@skypro.com")
    main_page_bonigarcia.add_phone("+7985899998787")
    main_page_bonigarcia.add_zipcode("")
    main_page_bonigarcia.add_city("Москва")
    main_page_bonigarcia.add_country("Россия")
    main_page_bonigarcia.add_jobposition("QA")
    main_page_bonigarcia.add_company("SkyPro")
    main_page_bonigarcia.push_button()
    class_first_name = main_page_bonigarcia.get_attribute_class_first_name()
    class_last_name = main_page_bonigarcia.get_attribute_class_last_name()
    class_address = main_page_bonigarcia.get_attribute_class_address()
    class_email = main_page_bonigarcia.get_attribute_class_email()
    class_phone = main_page_bonigarcia.get_attribute_class_phone()
    class_zipcode = main_page_bonigarcia.get_attribute_class_zipcode()
    class_city = main_page_bonigarcia.get_attribute_class_city()
    class_country = main_page_bonigarcia.get_attribute_class_country()
    class_jobposition = main_page_bonigarcia.get_attribute_class_jobposition()
    class_company = main_page_bonigarcia.get_attribute_class_company()

    main_page_bonigarcia.clouse_driver()

    assert class_first_name == "alert py-2 alert-success"
    assert class_last_name == "alert py-2 alert-success"
    assert class_address == "alert py-2 alert-success"
    assert class_email == "alert py-2 alert-success"
    assert class_phone == "alert py-2 alert-success"
    assert class_zipcode == "alert py-2 alert-danger"
    assert class_city == "alert py-2 alert-success"
    assert class_country == "alert py-2 alert-success"
    assert class_jobposition == "alert py-2 alert-success"
    assert class_company == "alert py-2 alert-success"



