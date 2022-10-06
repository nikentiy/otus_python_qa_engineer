from selenium import webdriver
from selenium.webdriver.common.by import By

from src.opencart_page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    HEADER = (By.XPATH, '//*[@id="content"]/h1')
    LOGIN_LNK = (By.XPATH, '//*[@id="content"]/p/a')
    SUBSCRIBE_NO_CHBX = (By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/label[2]/input')
    POLICY_CHBX = (By.XPATH, '//*[@id="content"]/form/div/div/input[1]')

    def __init__(self, driver: webdriver, base_path: str):
        super().__init__(driver, base_path)
        self.path = "".join([self.base_path, 'index.php?route=account/register'])

    def check_header(self):
        self.wait_for_element_visible(self.HEADER)

    def check_login_link(self):
        self.wait_for_element_clickable(self.LOGIN_LNK)

    def check_subscribe_no_chbx(self):
        self.wait_for_element_selection_state(self.SUBSCRIBE_NO_CHBX, True)

    def check_policy_chbx(self):
        self.wait_for_element_selection_state(self.POLICY_CHBX, False)