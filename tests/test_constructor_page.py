from locators import BurgerLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cnd


def test_navigate_stuff_tab(driver_logged_in, user):
    WebDriverWait(driver_logged_in, 5).until(cnd.visibility_of_element_located(BurgerLocators.stuff)).is_displayed()
    driver_logged_in.find_element(*BurgerLocators.stuff).click()
    WebDriverWait(driver_logged_in, 3).until(
        cnd.visibility_of_element_located(BurgerLocators.stuff_header))
    assert driver_logged_in.find_element(*BurgerLocators.current_tab).text == 'Начинки'


def test_navigate_burgers_tab(driver_logged_in, user):
    WebDriverWait(driver_logged_in, 5).until(cnd.visibility_of_element_located(BurgerLocators.burgers)).is_displayed()
    driver_logged_in.find_element(*BurgerLocators.stuff).click()
    driver_logged_in.find_element(*BurgerLocators.burgers).click()
    WebDriverWait(driver_logged_in, 3).until(
        cnd.visibility_of_element_located(BurgerLocators.burgers_header))
    assert driver_logged_in.find_element(*BurgerLocators.current_tab).text == 'Булки'


def test_navigate_souses_tab(driver_logged_in, user):
    WebDriverWait(driver_logged_in, 5).until(cnd.visibility_of_element_located(BurgerLocators.souses)).is_displayed()
    driver_logged_in.find_element(*BurgerLocators.souses).click()
    WebDriverWait(driver_logged_in, 3).until(
        cnd.visibility_of_element_located(BurgerLocators.souses_header))
    assert driver_logged_in.find_element(*BurgerLocators.current_tab).text == 'Соусы'
