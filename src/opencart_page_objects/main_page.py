import allure
from selenium.webdriver.common.by import By

from src.opencart_page_objects.base_page import BasePage


class MainPage(BasePage):
    LOGO = (By.XPATH, '//*[@id="logo"]')
    PRODUCTS_CAROUSEL = (By.XPATH, '//*[@id="content"]/div[1]')
    BANNER = (By.XPATH, '//*[@id="carousel0"]')
    CURRENCY_DROPDOWN = (By.XPATH, '//*[@id="form-currency"]/div/button')
    SYMBOL = (By.XPATH, '//*[@id="form-currency"]/div/button/strong')
    GBP = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/button')
    EUR = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/button')
    USD = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[3]/button')

    @allure.step("Check logo")
    def check_logo(self):
        self.wait_for_element_visible(self.LOGO)

    @allure.step("Check products carousel")
    def check_products_carousel(self):
        self.wait_for_element_visible(self.PRODUCTS_CAROUSEL)

    @allure.step("Check banner")
    def check_banner(self):
        self.wait_for_element_visible(self.BANNER)

    @allure.step("Set currency")
    def set_currency(self, currency: str):
        self.element(self.CURRENCY_DROPDOWN).click()
        if currency == 'GBP':
            self.element(self.GBP).click()
            self.wait_for_text_on_element(self.SYMBOL, '£')
        elif currency == 'USD':
            self.element(self.USD).click()
            self.wait_for_text_on_element(self.SYMBOL, '$')
        elif currency == 'EUR':
            self.element(self.EUR).click()
            self.wait_for_text_on_element(self.SYMBOL, '€')
        else:
            assert ValueError(f'Unsupported currency {currency}')
