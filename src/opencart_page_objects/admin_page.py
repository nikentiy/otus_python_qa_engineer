from selenium import webdriver
from selenium.webdriver.common.by import By

from src.opencart_page_objects.base_page import BasePage


class AdminPage(BasePage):
    # LOGO = (By.XPATH, '//*[@id="header"]/div/a/img')
    LOGO = (By.XPATH, '//*[@id="header-logo"]')
    USERMANE = (By.XPATH, '//*[@id="input-username"]')
    PWD = (By.XPATH, '//*[@id="input-password"]')
    # LOGIN_BTN = (By.XPATH, '//*[@id="form-login"]/div[3]/button')
    LOGIN_BTN = (By.XPATH, '//*[@id="content"]/div/div/div/div/div[2]/form/div[3]/button')
    ERROR_MSG = (By.XPATH, '//*[@id="content"]/div/div/div/div/div[2]/div')
    CLOSE_ERR_BTN = (By.XPATH, '//*[@id="content"]/div/div/div/div/div[2]/div/button')

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
        self.username().send_keys(pwd)

    def close_error(self):
        self.element(self.CLOSE_ERR_BTN).click()
