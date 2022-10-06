from selenium.webdriver.common.by import By

from src.opencart_page_objects.base_page import BasePage


class MainPage(BasePage):
    LOGO = (By.XPATH, '//*[@id="logo"]')
    PRODUCTS_CAROUSEL = (By.XPATH, '//*[@id="content"]/div[1]')
    BANNER = (By.XPATH, '//*[@id="carousel0"]')

    def check_logo(self):
        self.wait_for_element_visible(self.LOGO)

    def check_products_carousel(self):
        self.wait_for_element_visible(self.PRODUCTS_CAROUSEL)

    def check_banner(self):
        self.wait_for_element_visible(self.BANNER)
