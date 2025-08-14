import pytest
from locators import RegistrationPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup")
class TestUserLogin:
    
    def test_successful_user_login(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 15)
        
        TEST_EMAIL = "lyamina_24@gmail.com"
        TEST_PASSWORD = "!QAZ2wsx"
        
        try:
            wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_BUTTON)).click()
            
            email_field = wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_FORM_EMAIL))
            email_field.clear()
            email_field.send_keys(TEST_EMAIL)
            
            password_field = wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_FORM_PASSWORD))
            password_field.clear()
            password_field.send_keys(TEST_PASSWORD)
            
            wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_SUBMIT_BUTTON)).click()
            
            wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.CREATE_AD_BUTTON))
            
            wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.USER_AVATAR))
            
            user_name = wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.USER_NAME))
            
            assert user_name.text == "User.", f"Ожидалось имя 'User.', получено '{user_name.text}'"
            
        except Exception as e:
            pytest.fail(f"Тест авторизации пользователя упал: {str(e)}")