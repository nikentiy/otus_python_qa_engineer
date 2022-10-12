import random
import string

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

    def login_btn(self):
        return self.element(self.LOGIN_BTN)

    def username(self):
        return self.element(self.USERMANE)

    def pwd(self):
        return self.element(self.PWD)

    def check_login_btn(self):
        self.wait_for_element_clickable(self.LOGIN_BTN)

    def click_login(self):
        self.login_btn().click()

    def check_logo(self):
        self.wait_for_element_visible(self.LOGO)

    def check_error_msg(self, is_present: bool = True):
        if not is_present:
            self.wait_for_element_invisible(self.ERROR_MSG)
        else:
            self.wait_for_element_visible(self.ERROR_MSG)

    def fill_username(self, username: str):
        self.username().send_keys(username)

    def fill_password(self, pwd: str):
        self.pwd().send_keys(pwd)

    def close_error(self):
        self.element(self.CLOSE_ERR_BTN).click()

    def login(self):
        self.fill_username('demo')
        self.fill_password('demo')
        self.click_login()
        self.wait_for_element_visible(self.DASHBOARD)

    def go_to_products_menu(self):
        self.wait_for_element_visible(self.CATALOG)
        self.element(self.CATALOG).click()
        self.wait_for_element_visible(self.PRODUCTS)
        self.element(self.PRODUCTS).click()

    def click_add_btn(self):
        self.wait_for_element_visible(self.ADD_BTN)
        self.element(self.ADD_BTN).click()

    def fill_general(self):
        self.wait_for_element_visible(self.PRODUCT_NAME_INP)
        self.element(self.PRODUCT_NAME_INP).send_keys(
            f'Best in The Best QA product {random_string(10)}')
        self.element(self.PRODUCT_NAME_INP).send_keys(f'test_{random_string(10)}')

    def fill_data(self):
        self.element(self.DATA_TAB).click()
        self.wait_for_element_visible(self.MODEL_INP)
        self.element(self.MODEL_INP).send_keys('noname')

    def apply_product(self):
        self.element(self.APPLY_BTN).click()
        self.wait_for_element_visible(self.ALERT)

    def select_first_product_in_list(self):
        self.element(self.FIRST_PRODUCT_CHBX).click()

    def click_delete_btn(self):
        self.element(self.DELETE_BTN).click()
