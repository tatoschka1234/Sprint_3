from locators import BurgerLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cnd


def test_navigate_to_profile(driver_logged_in, user):
    """
    Проверь переход по клику на «Личный кабинет».
    """
    WebDriverWait(driver_logged_in, 5).until(cnd.visibility_of_element_located(
        BurgerLocators.personal_account_button)).is_displayed()
    driver_logged_in.find_element(*BurgerLocators.personal_account_button).click()
    WebDriverWait(driver_logged_in, 5).until(cnd.visibility_of_element_located(
        BurgerLocators.profile_logout_button)).is_displayed()
    current_data = driver_logged_in.find_elements(*BurgerLocators.name_and_email_fields)
    assert current_data[0].get_attribute('value') == user.user_name
    assert current_data[1].get_attribute('value') == user.email


def test_profile_navigate_to_constuctor(driver_logged_in):
    """
    Проверь переход по клику на «Конструктор»
    """
    WebDriverWait(driver_logged_in, 5).until(cnd.visibility_of_element_located(
            BurgerLocators.personal_account_button)).is_displayed()
    driver_logged_in.find_element(*BurgerLocators.personal_account_button).click()
    WebDriverWait(driver_logged_in, 5).until(cnd.visibility_of_element_located(BurgerLocators.profile_logout_button)).is_displayed()
    driver_logged_in.find_element(*BurgerLocators.constructor_button).click()
    WebDriverWait(driver_logged_in, 5).until(cnd.url_to_be(BurgerLocators.main_url))
    assert driver_logged_in.current_url == BurgerLocators.main_url

def test_profile_navigate_to_logo(driver_logged_in):
    """
    Проверь переход по клику на логотип Stellar Burgers.
    """
    WebDriverWait(driver_logged_in, 5).until(cnd.visibility_of_element_located(
            BurgerLocators.personal_account_button)).is_displayed()
    driver_logged_in.find_element(*BurgerLocators.personal_account_button).click()
    WebDriverWait(driver_logged_in, 5).until(cnd.visibility_of_element_located(BurgerLocators.profile_logout_button)).is_displayed()
    driver_logged_in.find_element(*BurgerLocators.logo_button).click()
    WebDriverWait(driver_logged_in, 5).until(cnd.url_to_be(BurgerLocators.main_url))
    assert driver_logged_in.current_url == BurgerLocators.main_url


def test_profile_page_logout(driver_logged_in):
    """
    Проверь выход по кнопке «Выйти» в личном кабинете.
    """
    WebDriverWait(driver_logged_in, 5).until(cnd.visibility_of_element_located(
        BurgerLocators.personal_account_button)).is_displayed()
    driver_logged_in.find_element(*BurgerLocators.personal_account_button).click()
    WebDriverWait(driver_logged_in, 5).until(cnd.visibility_of_element_located(
        BurgerLocators.profile_logout_button)).is_displayed()
    driver_logged_in.find_element(*BurgerLocators.profile_logout_button).click()
    WebDriverWait(driver_logged_in, 5).until(cnd.url_to_be(BurgerLocators.login_url))
    assert driver_logged_in.current_url == BurgerLocators.login_url

