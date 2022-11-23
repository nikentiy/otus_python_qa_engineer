import allure
import pytest
from faker import Faker

from src.helper import random_string

faker = Faker()


@allure.title('Check main page')
def test_check_main_page(driver, main_page):
    driver.get(main_page.base_path)
    main_page.top()
    main_page.footer()
    main_page.check_logo()
    main_page.check_banner()
    main_page.check_products_carousel()


@allure.title('Check ability to switch currency')
@pytest.mark.parametrize("currency", ['GBP', 'EUR', 'USD'])
def test_switch_currency(driver, main_page, currency):
    driver.get(main_page.base_path)
    main_page.set_currency(currency)


@allure.title('Check catalog')
def test_check_catalog(driver, catalog_page):
    driver.get(catalog_page.path)
    catalog_page.top()
    catalog_page.footer()
    catalog_page.catalog()
    catalog_page.check_breadcrumb()
    catalog_page.check_compare_btn()
    catalog_page.check_cameras_link()


@allure.title('Check product pag')
def test_check_first_product_page(driver, product_page):
    driver.get(product_page.base_path)
    product_page.top()
    product_page.footer()
    product_page.open_product()
    product_page.check_add_btn()
    product_page.check_description_exist()
    product_page.check_specification_exist()
    product_page.check_reviews_exist()


@allure.title('Check admin page')
def test_check_admin_page(driver, admin_page):
    driver.get(admin_page.path)
    admin_page.check_logo()
    admin_page.check_login_btn()
    admin_page.click_login()
    admin_page.check_error_msg()
    admin_page.close_error()
    admin_page.check_error_msg(is_present=False)
    admin_page.fill_username('big bro')
    admin_page.fill_password('just Do 1t')


@allure.title('Check ability to add new product')
def test_add_new_product(driver, admin_page):
    driver.get(admin_page.path)
    admin_page.login()
    admin_page.go_to_products_menu()
    admin_page.click_add_btn()
    admin_page.fill_general()
    admin_page.fill_data()
    admin_page.apply_product()


@allure.title('Check ability to delete a product')
def test_delete_product(driver, admin_page):
    driver.get(admin_page.path)
    admin_page.login()
    admin_page.go_to_products_menu()
    admin_page.select_first_product_in_list()
    admin_page.click_delete_btn()


@allure.title('Check user registration page')
def test_check_user_registration_page(driver, registration_page):
    driver.get(registration_page.path)
    registration_page.top()
    registration_page.footer()
    registration_page.check_header()
    registration_page.check_login_link()
    registration_page.check_subscribe_no_chbx()
    registration_page.check_policy_chbx()


@allure.title('Check user registration flow')
def test_check_user_registration_flow(driver, registration_page):
    driver.get(registration_page.path)
    registration_page.fill_first_name(faker.first_name())
    registration_page.fill_last_name(faker.last_name())
    registration_page.fill_phone(faker.phone_number())
    registration_page.fill_email(faker.email())
    pwd = random_string(11)
    registration_page.fill_password(pwd)
    registration_page.fill_password_confirm(pwd)
    registration_page.click_continue()
