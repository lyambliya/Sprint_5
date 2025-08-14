from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "submitPassword")    
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    
    USER_AVATAR = (By.CSS_SELECTOR, "button[class='circleSmall']")
    USER_NAME = (By.CSS_SELECTOR, "h3[class='profileText name']")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")

    EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, "span.input_span__yWPqB") 
    EMAIL_ERROR_FIELD = (By.CSS_SELECTOR, "input[name='email'][class*='inputStandart']")
    PASSWORD_ERROR_FIELD = (By.CSS_SELECTOR, "input[name='password'][class*='inputStandart']")
    CONFIRM_PASSWORD_ERROR_FIELD = (By.CSS_SELECTOR, "input[name='submitPassword'][class*='inputStandart']")

    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]") 

    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")

    AUTH_MODAL_TITLE = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")

class AdCreationLocators:

    TITLE_FIELD = (By.NAME, "name")
    DESCRIPTION_FIELD = (By.NAME, "description")
    PRICE_FIELD = (By.NAME, "price")
    
    CATEGORY_DROPDOWN = (By.NAME, "category")
    CITY_DROPDOWN = (By.NAME, "city")
    
    CONDITION_NEW = (By.XPATH, "//input[@value='Новый']")
    CONDITION_USED = (By.XPATH, "//input[@value='Б/У']")
    
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    
    MY_ADS_SECTION = (By.XPATH, "//h1[contains(text(), 'Мои объявления')]")
    FIRST_AD_IN_LIST = (By.CSS_SELECTOR, "div.card")

    CATEGORY_OPTION = (By.XPATH, "//*[contains(text(), '{}')]")
    CITY_OPTION = (By.XPATH, "//*[contains(text(), '{}')]")

    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "button.arrowButton--right:not([disabled])")