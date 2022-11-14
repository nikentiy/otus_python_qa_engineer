import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.opencart_page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    HEADER = (By.XPATH, '//*[@id="content"]/h1')
    LOGIN_LNK = (By.XPATH, '//*[@id="content"]/p/a')
    SUBSCRIBE_NO_CHBX = (By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/label[2]/input')
    POLICY_CHBX = (By.XPATH, '//*[@id="content"]/form/div/div/input[1]')
    FIRST_NAME_INT = (By.XPATH, '//*[@id="input-firstname"]')
    LAST_NAME_INT = (By.XPATH, '//*[@id="input-lastname"]')
    EMAIL_INT = (By.XPATH, '//*[@id="input-email"]')
    PHONE_INT = (By.XPATH, '//*[@id="input-telephone"]')
    PHONE_INT = (By.XPATH, '//*[@id="input-telephone"]')
    PWD_INT = (By.XPATH, '//*[@id="input-password"]')
    PWD_C_INT = (By.XPATH, '//*[@id="input-confirm"]')
    CONTINUE_BTN = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')

    def __init__(self, driver: webdriver, base_path: str):
        super().__init__(driver, base_path)
        self.path = "".join([self.base_path, 'index.php?route=account/register'])

    @allure.step("Check header")
    def check_header(self):
        self.wait_for_element_visible(self.HEADER)

    @allure.step("Check login link")
    def check_login_link(self):
        self.wait_for_element_clickable(self.LOGIN_LNK)

    @allure.step("Check subscribe checkbox is set")
    def check_subscribe_no_chbx(self):
        self.wait_for_element_selection_state(self.SUBSCRIBE_NO_CHBX, True)

    @allure.step("Check policy checkbox is not set")
    def check_policy_chbx(self):
        self.wait_for_element_selection_state(self.POLICY_CHBX, False)

    @allure.step("Fill first user name")
    def fill_first_name(self, name: str):
        self.element(self.FIRST_NAME_INT).send_keys(name)

    @allure.step("Fill last user name")
    def fill_last_name(self, name: str):
        self.element(self.LAST_NAME_INT).send_keys(name)

    @allure.step("Fill user email")
    def fill_email(self, email: str):
        self.element(self.EMAIL_INT).send_keys(email)

    @allure.step("Fill user phone")
    def fill_phone(self, phone: str):
        self.element(self.PHONE_INT).send_keys(phone)

    @allure.step("Fill user password")
    def fill_password(self, pwd: str):
        self.element(self.PWD_INT).send_keys(pwd)

    @allure.step("Fill password confirm")
    def fill_password_confirm(self, pwd: str):
        self.element(self.PWD_C_INT).send_keys(pwd)

    @allure.step("Click continue button")
    def click_continue(self):
        self.element(self.CONTINUE_BTN).click()
