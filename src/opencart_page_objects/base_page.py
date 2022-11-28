import logging

import allure
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    TOP = (By.XPATH, '//*[@id="top"]')
    FOOTER = (By.XPATH, '/html/body/footer/div')

    def __init__(self, driver: webdriver, base_path: str):
        self.base_path = base_path
        self.driver = driver
        self.waiter = WebDriverWait(driver, 20)
        self.__config_logger()

    def __config_logger(self):
        log_console_format = "[%(levelname)s - %(asctime)s]: %(message)s"
        self.logger = logging.getLogger(type(self).__name__)
        console_logger = logging.StreamHandler()
        console_logger.setFormatter(logging.Formatter(log_console_format))
        self.logger.setLevel(level=logging.INFO)
        self.logger.addHandler(console_logger)

    def element(self, locator: tuple):
        self.logger.info(f"Finding an element: {locator}")
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name='not found element',
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"element '{locator}' has not been found")

    def wait_for_element_visible(self, locator: tuple):
        self.logger.info(f"Waiting for an element visible: {locator}")
        try:
            self.waiter.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name='timeout of element visibility',
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"element '{locator}' did not appear in time")

    def wait_for_element_invisible(self, locator: tuple):
        self.logger.info(f"Waiting for an element invisible: {locator}")
        try:
            self.waiter.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name='timeout of element invisibility',
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"element '{locator}' did not disappear in time")

    def wait_for_element_clickable(self, locator: tuple):
        self.logger.info(f"Waiting for an element clickable: {locator}")
        try:
            self.waiter.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name='timeout of element clickability',
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"element '{locator}' is not clickable in time")

    def wait_for_text_on_element(self, locator: tuple, text: str):
        self.logger.info(f"Waiting for text '{text}' on an element: {locator}")
        try:
            self.waiter.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name='timeout of waiting for test on an element',
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"text {text} did not appear on element '{locator}' in time")

    def wait_for_element_selection_state(self, locator: tuple, state: bool):
        self.logger.info(f"Waiting for selection state '{state}' of element:{locator}")
        element = self.element(locator)
        try:
            self.waiter.until(EC.element_selection_state_to_be(element, state))
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name='timeout of an element selection state',
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"element '{locator}' is not in expected selection: {state}")

    def top(self):
        self.wait_for_element_visible(self.TOP)

    def footer(self):
        self.wait_for_element_visible(self.FOOTER)
