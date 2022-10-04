import os

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", type=str, help="browser name"
    )
    parser.addoption(
        "--url", action="store",
        default="https://demo.opencart.com/", type=str,
        help="based url"
    )


@pytest.fixture(scope='class')
def base_url(request) -> str:
    return request.config.getoption("--url")


@pytest.fixture(scope='class')
def driver(request, base_url) -> webdriver:
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        caps = webdriver.DesiredCapabilities.CHROME.copy()
        caps['acceptInsecureCerts'] = True
        driver = webdriver.Chrome(desired_capabilities=caps)
    elif browser == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        driver = webdriver.Firefox(firefox_profile=profile)
    elif browser == "opera":
        driver = webdriver.Opera()
    else:
        raise Exception(f"Unsupported browser {browser}")
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope='class')
def waiter(driver) -> WebDriverWait:
    return WebDriverWait(driver, 20)
