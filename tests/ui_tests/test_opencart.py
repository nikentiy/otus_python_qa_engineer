from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

TOP = '//*[@id="top"]'
FOOTER = '/html/body/footer/div'


def test_check_main_page(driver, main_page):
    driver.get(main_page.base_path)
    main_page.top()
    main_page.footer()
    main_page.check_logo()
    main_page.check_banner()
    main_page.check_products_carousel()


def test_check_catalog(driver, catalog_page):
    driver.get(catalog_page.path)
    catalog_page.top()
    catalog_page.footer()
    catalog_page.catalog()
    catalog_page.check_breadcrumb()
    catalog_page.check_compare_btn()
    catalog_page.check_cameras_link()


def test_check_first_product_page(driver, product_page):
    driver.get(product_page.base_path)
    product_page.top()
    product_page.footer()
    product_page.open_product()
    product_page.check_add_btn()
    product_page.check_description_exist()
    product_page.check_specification_exist()
    product_page.check_reviews_exist()


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


def test_check_user_registration_page(driver, registration_page):
    driver.get(registration_page.path)
    registration_page.top()
    registration_page.footer()
    registration_page.check_header()
    registration_page.check_login_link()
    registration_page.check_subscribe_no_chbx()
    registration_page.check_policy_chbx()
