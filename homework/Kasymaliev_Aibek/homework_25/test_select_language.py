from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(select)
    dropdown.select_by_value('1')
    choose_language = dropdown.first_selected_option.text
    driver.find_element(By.ID, 'submit-id-submit').click()
    result = driver.find_element(By.ID, 'result-text').text
    assert choose_language == result, f"Ошибка! Ожидали {choose_language}, получили {result}"
