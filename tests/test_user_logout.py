import pytest
from locators import RegistrationPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup")
class TestUserLogout:
    
    def test_user_logout_flow(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 15)
        
        TEST_EMAIL = "lyamina_24@gmail.com"
        TEST_PASSWORD = "!QAZ2wsx"
        
        try:
            wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_BUTTON)).click()
            
            wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_FORM_EMAIL)).send_keys(TEST_EMAIL)
            
            wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_FORM_PASSWORD)).send_keys(TEST_PASSWORD)
            
            wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_SUBMIT_BUTTON)).click()
            
            wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.LOGOUT_BUTTON))
            
            wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.LOGOUT_BUTTON)).click()
            
            wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_BUTTON))
            
            assert len(driver.find_elements(*RegistrationPageLocators.USER_AVATAR)) == 0, \
                "Аватар пользователя остался на странице после выхода"
            
            assert len(driver.find_elements(*RegistrationPageLocators.USER_NAME)) == 0, \
                "Имя пользователя осталось на странице после выхода"
            
            wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.CREATE_AD_BUTTON))
            
        except Exception as e:
            pytest.fail(f"Тест завершился с ошибкой: {str(e)}")