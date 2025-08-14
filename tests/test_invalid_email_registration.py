import pytest
from locators import RegistrationPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup")
class TestInvalidEmailRegistration:
    
    @pytest.mark.parametrize("invalid_email", [
        "plaintext",
        "missing@domain",
        "invalid@domain.",
        "@missinglocal.com"
    ])
    def test_fields_highlighted_on_invalid_email(self, setup, invalid_email):
        driver = setup
        wait = WebDriverWait(driver, 15) 
        
        try:
            login_button = wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_BUTTON))
            login_button.click()

            no_account_button = wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON))
            no_account_button.click()

            email_field = wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_FIELD))
            email_field.clear()
            email_field.send_keys(invalid_email)

            create_button = wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON))
            create_button.click()

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
            pytest.fail(f"Тест упал на email '{invalid_email}': {str(e)}")