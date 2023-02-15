from locators import BurgerLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cnd


def test_register_correct_data(driver, user):
    driver.get(BurgerLocators.register_url)
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(BurgerLocators.psw_reg_field)).is_displayed()
    reg_fields = driver.find_elements(*BurgerLocators.name_and_email_fields)
    reg_fields[0].send_keys(user.user_name)
    reg_fields[1].send_keys(user.email)
    driver.find_element(*BurgerLocators.psw_reg_field).send_keys(user.password)
    driver.find_element(*BurgerLocators.button_register).click()


def test_register_incorrect_password(driver, user):
    driver.get(BurgerLocators.register_url)
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(
        BurgerLocators.psw_reg_field)).is_displayed()
    reg_fields = driver.find_elements(*BurgerLocators.name_and_email_fields)
    reg_fields[0].send_keys(user.user_name)
    reg_fields[1].send_keys(user.email)
    driver.find_element(*BurgerLocators.psw_reg_field).send_keys("1")
    driver.find_element(*BurgerLocators.button_register).click()
    assert driver.find_element(*BurgerLocators.bad_password).text == 'Некорректный пароль'


def test_register_incorrect_username(driver, user):
    driver.get(BurgerLocators.register_url)
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(BurgerLocators.psw_reg_field)).is_displayed()
    reg_fields = driver.find_elements(*BurgerLocators.name_and_email_fields)
    reg_fields[1].send_keys(user.email)
    driver.find_element(*BurgerLocators.psw_reg_field).send_keys(user.password)
    driver.find_element(*BurgerLocators.button_register).click()
    assert driver.current_url == BurgerLocators.register_url


def test_register_incorrect_email(driver, user):
    driver.get(BurgerLocators.register_url)
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(BurgerLocators.psw_reg_field)).is_displayed()
    reg_fields = driver.find_elements(*BurgerLocators.name_and_email_fields)
    reg_fields[0].send_keys(user.user_name)
    reg_fields[1].send_keys(user.user_name)
    driver.find_element(*BurgerLocators.psw_reg_field).send_keys(user.password)
    driver.find_element(*BurgerLocators.button_register).click()
    assert driver.current_url == BurgerLocators.register_url