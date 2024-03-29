import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.opencart_page_objects.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[1]/a/img')
    ADD_BTN = (By.XPATH, '//*[@id="button-cart"]')
    PRODUCT_INFO = (By.XPATH, '//*[@id="content"]/div/div[1]/ul[2]')

    @allure.step("Get product")
    def product(self):
        return self.element(self.PRODUCT)

    @allure.step("Open product page")
    def open_product(self):
        self.product().click()

    @allure.step("Check add button")
    def check_add_btn(self):
        self.wait_for_element_clickable(self.ADD_BTN)

    @allure.step("Check the product description exists")
    def check_description_exist(self):
        self.wait_for_text_on_element(self.PRODUCT_INFO, 'Description')

    @allure.step("Check product specification exists")
    def check_specification_exist(self):
        self.wait_for_text_on_element(self.PRODUCT_INFO, 'Specification')

    @allure.step("Check product reviews exists")
    def check_reviews_exist(self):
        self.wait_for_text_on_element(self.PRODUCT_INFO, 'Reviews')
