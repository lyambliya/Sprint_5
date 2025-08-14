import pytest
from locators import RegistrationPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from random import randint

@pytest.mark.usefixtures("setup")
class TestRegistration:

    def test_successful_registration(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 10)

        login_button = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_BUTTON))
        login_button.click()

        no_account_button = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON))
        no_account_button.click()

        email = f"test{randint(1000, 9999)}@example.com"
        
        email_field = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_FIELD))
        email_field.send_keys(email)

        password_field = driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD)
        password_field.send_keys("TestPassword123")

        confirm_password_field = driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys("TestPassword123")  

        create_account_button = driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
        create_account_button.click()

        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.USER_AVATAR))
        user_name = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.USER_NAME))

        assert user_name.text == "User."  
        assert driver.find_element(*RegistrationPageLocators.CREATE_AD_BUTTON).is_displayed()