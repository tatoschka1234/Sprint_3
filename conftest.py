import pytest
from selenium import webdriver
from locators import BurgerLocators


class User:
    user_name = "Nata"
    password = "123456"
    email = "nata_kkk_3478@yandex.ru"

    # def generate_new_login(self):
    #     self.email = "fawlefm"
    #
    # def generate_new_psw(self):
    #     self.password = "fawlefm"
    #
    # def generate_email(self):
    #     self.email = f"nata_kkk_3{randint(000, 999)}@yandex.ru"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def driver_logged_in():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(BurgerLocators.login_url)
    user = User()
    reg_fields = driver.find_elements(*BurgerLocators.name_and_email_fields)
    reg_fields[0].send_keys(user.email)
    driver.find_element(*BurgerLocators.psw_reg_field).send_keys(user.password)
    driver.find_element(*BurgerLocators.button_login).click()
    yield driver
    driver.quit()


@pytest.fixture
def user():
    user = User()
    yield user
