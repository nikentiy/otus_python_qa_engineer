from selenium import webdriver
from selenium.common import NoSuchElementException
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

    def element(self, locator: tuple):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            AssertionError(f"element '{locator}' has not been found")

    def wait_for_element_visible(self, locator: tuple):
        try:
            self.waiter.until(EC.visibility_of_element_located(locator))
        except TimeoutError:
            AssertionError(f"element '{locator}' did not appear in time")

    def wait_for_element_invisible(self, locator: tuple):
        try:
            self.waiter.until(EC.invisibility_of_element_located(locator))
        except TimeoutError:
            AssertionError(f"element '{locator}' did not disappear in time")

    def wait_for_element_clickable(self, locator: tuple):
        try:
            self.waiter.until(EC.element_to_be_clickable(locator))
        except TimeoutError:
            AssertionError(f"element '{locator}' is not clickable in time")

    def wait_for_text_on_element(self, locator: tuple, text: str):
        try:
            self.waiter.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutError:
            AssertionError(f"text {text} did not appear on element '{locator}' in time")

    def wait_for_element_selection_state(self, locator: tuple, state: bool):
        element = self.element(locator)
        try:
            self.waiter.until(EC.element_selection_state_to_be(element, state))
        except TimeoutError:
            AssertionError(f"element '{locator}' is not in expected selection: {state}")

    def top(self):
        self.wait_for_element_visible(self.TOP)

    def footer(self):
        self.wait_for_element_visible(self.FOOTER)
