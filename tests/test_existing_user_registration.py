import pytest
from locators import RegistrationPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup")
class TestExistingUserRegistration:
    
    def test_existing_user_registration_error(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 15)
        
        EXISTING_EMAIL = "lyamina_24@gmail.com"
        EXISTING_PASSWORD = "!QAZ2wsx"
        
        try:
            wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_BUTTON)).click()
            
            wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)).click()
            
            email_field = wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_FIELD))
            email_field.clear()
            email_field.send_keys(EXISTING_EMAIL)
            
            password_field = wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_FIELD))
            password_field.clear()
            password_field.send_keys(EXISTING_PASSWORD)
            
            confirm_field = wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.CONFIRM_PASSWORD_FIELD))
            confirm_field.clear()
            confirm_field.send_keys(EXISTING_PASSWORD)
            
            wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)).click()
            
            wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR_FIELD))
            wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR_FIELD))
            wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.CONFIRM_PASSWORD_ERROR_FIELD))
        
            error_message = wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR_MESSAGE))
            assert "Ошибка" in error_message.text, f"Ожидалось 'Ошибка', получено '{error_message.text}'"
            
        except Exception as e:
            pytest.fail(f"Тест упал: {str(e)}")