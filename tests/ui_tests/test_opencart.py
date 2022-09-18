from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

TOP = '//*[@id="top"]'
FOOTER = '/html/body/footer/div'


def test_check_main_page(driver, waiter, base_url):
    driver.get(base_url)
    logo_xpath = '//*[@id="logo"]'
    products_carousel = '//*[@id="carousel-banner-0"]'
    banner = '//*[@id="carousel-banner-1"]'
    waiter.until(EC.visibility_of_element_located((By.XPATH, TOP)))
    waiter.until(EC.visibility_of_element_located((By.XPATH, FOOTER)))
    waiter.until(EC.visibility_of_element_located((By.XPATH, logo_xpath)))
    waiter.until(EC.visibility_of_all_elements_located((By.XPATH, products_carousel)))
    waiter.until(EC.visibility_of_all_elements_located((By.XPATH, banner)))


def test_check_catalog(driver, base_url, waiter):
    url = "".join([base_url, 'index.php?route=product/category&language=en-gb&path=18'])
    catalog = '//*[@id="column-left"]'
    breadcrumb = '//*[@id="product-category"]/ul'
    cameras_link = '//*[@id="narbar-menu"]/ul/li[7]/a'
    compare_btn = '//*[@id="compare-total"]'
    driver.get(url)
    waiter.until(EC.visibility_of_element_located((By.XPATH, TOP)))
    waiter.until(EC.visibility_of_element_located((By.XPATH, FOOTER)))
    driver.find_element(By.XPATH, catalog)
    waiter.until(EC.visibility_of_element_located((By.XPATH, breadcrumb)))
    waiter.until(EC.element_to_be_clickable((By.XPATH, compare_btn)))
    waiter.until(EC.element_to_be_clickable((By.XPATH, cameras_link)))


def test_check_first_product_page(driver, base_url, waiter):
    product = '//*[@id="content"]/div[2]/div[1]/form/div'
    add_button = '//*[@id="button-cart"]'
    product_info = '//*[@id="content"]/ul'
    driver.get(base_url)
    waiter.until(EC.visibility_of_element_located((By.XPATH, TOP)))
    waiter.until(EC.visibility_of_element_located((By.XPATH, FOOTER)))
    driver.find_element(By.XPATH, product).click()
    waiter.until(EC.element_to_be_clickable((By.XPATH, add_button)))
    waiter.until(EC.text_to_be_present_in_element((By.XPATH, product_info),
                                                  'Description'))
    waiter.until(EC.text_to_be_present_in_element((By.XPATH, product_info),
                                                  'Specification'))
    waiter.until(EC.text_to_be_present_in_element((By.XPATH, product_info),
                                                  'Reviews'))


def test_check_admin_page(driver, base_url, waiter):
    url = "".join([base_url, 'admin'])
    driver.get(url)
    logo = '//*[@id="header"]/div/a/img'
    username = '//*[@id="input-username"]'
    pwd = '//*[@id="input-password"]'
    login_btn = '//*[@id="form-login"]/div[3]/button'
    error_msg = '//*[@id="alert"]/div'
    waiter.until(EC.visibility_of_element_located((By.XPATH, logo)))
    waiter.until(EC.element_to_be_clickable((By.XPATH, login_btn)))
    driver.find_element(By.XPATH, login_btn).click()
    waiter.until(EC.visibility_of_element_located((By.XPATH, error_msg)))
    waiter.until(EC.invisibility_of_element_located((By.XPATH, error_msg)))
    driver.find_element(By.XPATH, username).send_keys('big bro')
    driver.find_element(By.XPATH, pwd).send_keys('just Do 1t')


def test_check_user_registration_page(driver, base_url, waiter):
    url = "".join([base_url, 'index.php?route=account/register'])
    driver.get(url)
    header = '//*[@id="content"]/h1'
    login_link = '//*[@id="content"]/p/a'
    subscribe_no_checkbox = '//*[@id="input-newsletter-no"]'
    policy_checkbox = '//*[@id="form-register"]/div/div/div/input'
    waiter.until(EC.visibility_of_element_located((By.XPATH, TOP)))
    waiter.until(EC.visibility_of_element_located((By.XPATH, FOOTER)))
    waiter.until(EC.visibility_of_element_located((By.XPATH, header)))
    waiter.until(EC.element_to_be_clickable((By.XPATH, login_link)))
    waiter.until(EC.element_selection_state_to_be(
        driver.find_element(By.XPATH, subscribe_no_checkbox), True))
    waiter.until(EC.element_selection_state_to_be(
        driver.find_element(By.XPATH, policy_checkbox), False))
