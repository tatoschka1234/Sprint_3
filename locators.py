from selenium.webdriver.common.by import By


class BurgerLocators:
    main_url = "https://stellarburgers.nomoreparties.site/"
    register_url = f"{main_url}register"
    login_url = f"{main_url}login"
    forgot_psw_url = f"{main_url}forgot-password"

    login_link = By.XPATH, ".//a[text()='Войти']"

    name_and_email_fields = By.XPATH, ".//input[@type='text']"
    psw_reg_field = By.XPATH, ".//input[@type='password']"
    button_register = By.XPATH, ".//button[text()='Зарегистрироваться']"

    button_login = By.XPATH, ".//button[text()='Войти']"
    button_account_login = By.XPATH, ".//button[text()='Войти в аккаунт']"
    button_restore_psw = By.XPATH, ".//button[text()='Восстановить']"

    personal_account_button = By.XPATH, ".//a[contains(@href, '/account')]"
    profile = By.XPATH, ".//a[contains(@href, '/account/profile')]"
    profile_logout_button = By.XPATH, ".//button[text()='Выход']"

    constructor_button = By.XPATH, ".//p[text()='Конструктор']"
    logo_button = By.XPATH, ".//*[contains(@class, 'AppHeader_header__logo')]"

    burgers = By.XPATH, ".//span[text()='Булки']"
    burgers_header = By.XPATH, ".//h2[text()='Булки']"
    souses = By.XPATH, ".//span[text()='Соусы']"
    souses_header = By.XPATH, "//h2[text()='Соусы']"
    stuff = By.XPATH, ".//span[text()='Начинки']"
    stuff_header = By.XPATH, ".//h2[text()='Начинки']"
    current_tab = By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]/span"

    bad_password = By.CLASS_NAME, "input__error"
