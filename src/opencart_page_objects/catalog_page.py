from selenium import webdriver
from selenium.webdriver.common.by import By

from src.opencart_page_objects.base_page import BasePage


class CatalogPage(BasePage):
    CATALOG = (By.XPATH, '//*[@id="column-left"]')
    BREADCRUMB = (By.XPATH, '//*[@id="product-category"]/ul')
    CAMERAS_LINK = (By.XPATH, '//*[@id="narbar-menu"]/ul/li[7]/a')
    COMPARE_BTN = (By.XPATH, '//*[@id="compare-total"]')

    def __init__(self, driver: webdriver, base_path: str):
        super().__init__(driver, base_path)
        self.path = "".join([self.base_path,
                        'index.php?route=product/category&language=en-gb&path=18'])

    def catalog(self):
        return self.element(self.CATALOG)

    def check_breadcrumb(self):
        self.wait_for_element_visible(self.BREADCRUMB)

    def check_compare_btn(self):
        self.wait_for_element_clickable(self.BREADCRUMB)

    def check_cameras_link(self):
        self.wait_for_element_clickable(self.COMPARE_BTN)
