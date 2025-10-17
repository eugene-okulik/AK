import os


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_registration_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    user_first_name = driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]')
    user_first_name.send_keys('Potter')
    user_last_name = driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]')
    user_last_name.send_keys('Harry')
    user_email = driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]')
    user_email.send_keys('buklya@mail.ru')
    driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]').click()
    user_mobile = driver.find_element(By.ID, 'userNumber')
    user_mobile.send_keys('79998887766')
    bithday_date = driver.find_element(By.ID, 'dateOfBirthInput')
    driver.execute_script("arguments[0].scrollIntoView();", bithday_date)
    bithday_date.click()
    driver.find_element(By.XPATH, '//*[@class="react-datepicker__month-select"]').click()
    driver.find_element(By.XPATH, '//option[@value="0"]').click()
    driver.find_element(By.XPATH, '//select[@class="react-datepicker__year-select"]').click()
    driver.find_element(By.XPATH, '//option[@value="1999"]').click()
    driver.find_element(By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--001"]').click()
    user_subject = driver.find_element(By.ID, 'subjectsInput')
    user_subject.send_keys('Potions')
    hobbies = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-2"]')
    driver.execute_script("arguments[0].scrollIntoView();", hobbies)
    hobbies.click()
    download_file = driver.find_element(By.ID, 'uploadPicture')
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, 'data', 'qa.jpg')
    download_file.send_keys(file_path)
    user_address = driver.find_element(By.ID, 'currentAddress')
    user_address.send_keys('The Cupboard under the Stairs, 4 Privet Drive, Little Whinging, Surrey, England')
    state = driver.find_element(By.ID, 'react-select-3-input')
    state.send_keys('NCR')
    wait = WebDriverWait(driver, 5)
    options = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[contains(@id, "react-select-3-option") and text()="NCR"] '))
    )
    options.click()
    driver.find_element(By.ID, 'city').click()
    select_city = wait.until(EC.visibility_of_element_located((By.ID, 'react-select-4-option-1')))
    select_city.click()
    driver.find_element(By.ID, 'submit').click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//table[@class="table table-dark table-striped table-bordered table-hover"]'))
    )
    text_forms = driver.find_elements(By.TAG_NAME, 'tr')
    for text in text_forms:
        print(text.text)
