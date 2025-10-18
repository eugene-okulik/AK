from selenium.webdriver.common.by import By


def test_check_search_text(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_input = driver.find_element(By.NAME, 'text_string')
    text_input.send_keys('Py')
    text_input.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    print(result_text.text)
