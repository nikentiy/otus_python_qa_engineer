import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from src.opencart_page_objects.admin_page import AdminPage
from src.opencart_page_objects.catalog_page import CatalogPage
from src.opencart_page_objects.main_page import MainPage
from src.opencart_page_objects.product_page import ProductPage
from src.opencart_page_objects.registration_page import RegistrationPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", type=str, help="browser name"
    )
    parser.addoption(
        "--executor", action="store", default="localhost", type=str,
        help="a way to execute tests"
    )
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--videos", action="store_true")
    parser.addoption("--bv")
    parser.addoption(
        "--url", action="store",
        default="http://demo3x.opencartreports.com/", type=str,
        help="based url"
    )


@pytest.fixture(scope='class')
def base_url(request) -> str:
    return request.config.getoption("--url")


@pytest.fixture(scope='class')
def driver(request, base_url) -> webdriver:
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    executor_url = f"http://{executor}:4444/wd/hub"

    if executor == "local":
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
    else:
        caps = {
            "browserName": browser,
            "browserVersion": version,
            "name": "Nikentiy",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'goog:chromeOptions': {}
        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope='class')
def waiter(driver) -> WebDriverWait:
    return WebDriverWait(driver, 20)


@pytest.fixture(scope='class')
def main_page(driver, base_url):
    return MainPage(driver, base_url)


@pytest.fixture(scope='class')
def catalog_page(driver, base_url):
    return CatalogPage(driver, base_url)


@pytest.fixture(scope='class')
def product_page(driver, base_url):
    return ProductPage(driver, base_url)


@pytest.fixture(scope='class')
def admin_page(driver, base_url):
    return AdminPage(driver, base_url)


@pytest.fixture(scope='class')
def registration_page(driver, base_url):
    return RegistrationPage(driver, base_url)
