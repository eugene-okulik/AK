from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def test_add_card(driver):
    driver.get('http://testshop.qa-practice.com/')
    actions = ActionChains(driver)
    desk_link = driver.find_element(By.LINK_TEXT, 'Customizable Desk')
    actions.key_down(Keys.CONTROL).click(desk_link).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.ID, 'add_to_cart').click()
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-content"]'))
    )
    driver.find_element(By.XPATH, '//button[@class="btn btn-secondary"]').click()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(
        By.XPATH, '//*[@class="o_navlink_background btn position-relative rounded-circle p-1 text-center text-reset"]'
    ).click()
    order = driver.find_element(By.XPATH, '//*[@class="d-inline align-top h6 fw-bold"]').text
    print(order)
    assert order == 'Customizable Desk (Steel, White)', \
        f'Ошибка! Ожидали: Customizable Desk (Steel, White), получиили {order}'


def test_pop_up(driver):
    driver.get('http://testshop.qa-practice.com/')
    desc = driver.find_element(By.XPATH, '//*[@class="img img-fluid h-100 w-100 position-absolute"]')
    ActionChains(driver).move_to_element(desc)
    driver.find_element(By.XPATH, '//*[@class="btn btn-primary a-submit"]').click()
    wait = WebDriverWait(driver, 10)
    desc_text = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@class="product-name product_display_name"]'))
    ).text
    print(desc_text)
    assert desc_text == '[FURN_0096] Customizable Desk (Steel, White)' == desc_text, \
        f'Ошибка! Ожидали: Customizable Desk (Steel, White), получиили {desc_text}'
