from locators import BurgerLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cnd


def test_main_page_account_login(driver, user):
    """
    вход по кнопке Войти в аккаунт на главной
    """
    driver.get(BurgerLocators.main_url)
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(
        BurgerLocators.button_account_login)).is_displayed()
    driver.find_element(*BurgerLocators.button_account_login).click()
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(BurgerLocators.psw_reg_field)).is_displayed()
    reg_fields = driver.find_elements(*BurgerLocators.name_and_email_fields)
    reg_fields[0].send_keys(user.email)
    driver.find_element(*BurgerLocators.psw_reg_field).send_keys(user.password)
    driver.find_element(*BurgerLocators.button_login).click()
    WebDriverWait(driver, 5).until(cnd.url_to_be(BurgerLocators.main_url))
    assert driver.current_url == BurgerLocators.main_url


def test_profile_account_login(driver, user):
    """
    вход через кнопку Личный кабинет
    """
    driver.get(BurgerLocators.main_url)
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(
        BurgerLocators.personal_account_button)).is_displayed()
    driver.find_element(*BurgerLocators.personal_account_button).click()
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(BurgerLocators.psw_reg_field)).is_displayed()
    reg_fields = driver.find_elements(*BurgerLocators.name_and_email_fields)
    reg_fields[0].send_keys(user.email)
    driver.find_element(*BurgerLocators.psw_reg_field).send_keys(user.password)
    driver.find_element(*BurgerLocators.button_login).click()
    WebDriverWait(driver, 5).until(cnd.url_to_be(BurgerLocators.main_url))
    assert driver.current_url == BurgerLocators.main_url

def test_login_from_register_page(driver, user):
    """
    вход через кнопку в форме регистрации
    """
    driver.get(BurgerLocators.register_url)
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(
        BurgerLocators.button_register)).is_displayed()
    driver.find_element(*BurgerLocators.login_link).click()
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(BurgerLocators.psw_reg_field)).is_displayed()
    reg_fields = driver.find_elements(*BurgerLocators.name_and_email_fields)
    reg_fields[0].send_keys(user.email)
    driver.find_element(*BurgerLocators.psw_reg_field).send_keys(user.password)
    driver.find_element(*BurgerLocators.button_login).click()
    WebDriverWait(driver, 5).until(cnd.url_to_be(BurgerLocators.main_url))
    assert driver.current_url == BurgerLocators.main_url

def test_login_from_forgot_psw(driver, user):
    """
    вход через кнопку в форме восстановления пароля
    """
    driver.get(BurgerLocators.forgot_psw_url)
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(
        BurgerLocators.button_restore_psw)).is_displayed()
    driver.find_element(*BurgerLocators.login_link).click()
    WebDriverWait(driver, 5).until(cnd.visibility_of_element_located(BurgerLocators.psw_reg_field)).is_displayed()
    reg_fields = driver.find_elements(*BurgerLocators.name_and_email_fields)
    reg_fields[0].send_keys(user.email)
    driver.find_element(*BurgerLocators.psw_reg_field).send_keys(user.password)
    driver.find_element(*BurgerLocators.button_login).click()
    WebDriverWait(driver, 5).until(cnd.url_to_be(BurgerLocators.main_url))
    assert driver.current_url == BurgerLocators.main_url


def test_login_incorrect_password(driver, user):
    driver.get(BurgerLocators.login_url)
    reg_fields = driver.find_elements(*BurgerLocators.name_and_email_fields)
    reg_fields[0].send_keys(user.email)
    driver.find_element(*BurgerLocators.psw_reg_field).send_keys(
        f"{user.password}12")
    driver.find_element(*BurgerLocators.button_login).click()
    assert driver.current_url == BurgerLocators.login_url