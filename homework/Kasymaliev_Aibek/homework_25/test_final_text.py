from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_text(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.XPATH, '//button[text()="Start"]').click()
    wait = WebDriverWait(driver, 10)
    result_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//h4[text()="Hello World!"]')))
    assert result_text.text == 'Hello World!', f"Ошибка!, ожидали 'Hello World!', получили {result_text.text}"
