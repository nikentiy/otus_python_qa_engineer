import allure

from selenium import webdriver
from selenium.webdriver.common.by import By

from src.helper import random_string
from src.opencart_page_objects.base_page import BasePage


class AdminPage(BasePage):
    LOGO = (By.XPATH, '//*[@id="header-logo"]')
    USERMANE = (By.XPATH, '//*[@id="input-username"]')
    PWD = (By.XPATH, '//*[@id="input-password"]')
    LOGIN_BTN = (By.XPATH, '//*[@id="content"]/div/div/div/div/div[2]/form/div[3]/button')
    ERROR_MSG = (By.XPATH, '//*[@id="content"]/div/div/div/div/div[2]/div')
    CLOSE_ERR_BTN = (By.XPATH, '//*[@id="content"]/div/div/div/div/div[2]/div/button')
    DASHBOARD = (By.XPATH, '//*[@id="content"]/div[1]/div/h1')
    CATALOG = (By.XPATH, '//*[@id="menu-catalog"]')
    PRODUCTS = (By.XPATH, '//*[@id="collapse1"]/li[2]')
    ADD_BTN = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a')
    PRODUCT_NAME_INP = (By.XPATH, '//*[@id="input-name1"]')
    PRODUCT_META_INP = (By.XPATH, '//*[@id="input-meta-title1"]')
    DATA_TAB = (By.XPATH, '//*[@id="priceInitialize"]')
    MODEL_INP = (By.XPATH, '//*[@id="input-model"]')
    APPLY_BTN = (By.XPATH, '//*[@id="save_apply"]')
    ALERT = (By.XPATH, '//*[@id="content"]/div[2]/div[1]')
    FIRST_PRODUCT_CHBX = (By.XPATH, '//*[@id="form-product"]/div/table/tbody/tr[1]/td[1]/input')
    DELETE_BTN = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]')

    def __init__(self, driver: webdriver, base_path: str):
        super().__init__(driver, base_path)
        self.path = "".join([self.base_path, 'admin'])

    @allure.step("Get login button")
    def login_btn(self):
        return self.element(self.LOGIN_BTN)

    @allure.step("Get username field")
    def username(self):
        return self.element(self.USERMANE)

    @allure.step("Get password field")
    def pwd(self):
        return self.element(self.PWD)

    @allure.step("Check login button")
    def check_login_btn(self):
        self.wait_for_element_clickable(self.LOGIN_BTN)

    @allure.step("Click login button")
    def click_login(self):
        self.login_btn().click()

    @allure.step("Check logo")
    def check_logo(self):
        self.wait_for_element_visible(self.LOGO)

    @allure.step("Check error message")
    def check_error_msg(self, is_present: bool = True):
        if not is_present:
            self.wait_for_element_invisible(self.ERROR_MSG)
        else:
            self.wait_for_element_visible(self.ERROR_MSG)

    @allure.step("Fill username")
    def fill_username(self, username: str):
        self.username().send_keys(username)

    @allure.step("Fill password")
    def fill_password(self, pwd: str):
        self.pwd().send_keys(pwd)

    @allure.step("Close error message")
    def close_error(self):
        self.element(self.CLOSE_ERR_BTN).click()

    @allure.step("Login as admin")
    def login(self):
        self.fill_username('demo')
        self.fill_password('demo')
        self.click_login()
        self.wait_for_element_visible(self.DASHBOARD)

    @allure.step("Open products menu")
    def go_to_products_menu(self):
        self.wait_for_element_visible(self.CATALOG)
        self.element(self.CATALOG).click()
        self.wait_for_element_visible(self.PRODUCTS)
        self.element(self.PRODUCTS).click()

    @allure.step("Click add product button")
    def click_add_btn(self):
        self.wait_for_element_visible(self.ADD_BTN)
        self.element(self.ADD_BTN).click()

    @allure.step("Fill general product info")
    def fill_general(self, data: str = f'test_{random_string(10)}'):
        self.wait_for_element_visible(self.PRODUCT_NAME_INP)
        self.element(self.PRODUCT_NAME_INP).send_keys(
            f'Best in The Best QA product {random_string(10)}')
        self.element(self.PRODUCT_NAME_INP).send_keys(data)

    @allure.step("Fill product data")
    def fill_data(self, data: str = 'noname'):
        self.element(self.DATA_TAB).click()
        self.wait_for_element_visible(self.MODEL_INP)
        self.element(self.MODEL_INP).send_keys(data)

    @allure.step("Apply a product")
    def apply_product(self):
        self.element(self.APPLY_BTN).click()
        self.wait_for_element_visible(self.ALERT)

    @allure.step("Select first product in the list")
    def select_first_product_in_list(self):
        self.element(self.FIRST_PRODUCT_CHBX).click()

    @allure.step("Click delete product button")
    def click_delete_btn(self):
        self.element(self.DELETE_BTN).click()
