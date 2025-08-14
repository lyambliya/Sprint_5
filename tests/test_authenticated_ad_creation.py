import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import RegistrationPageLocators, AdCreationLocators
import time

class TestAdCreation:
    @pytest.mark.usefixtures("setup")
    def test_create_new_ad(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        actions = ActionChains(driver)
        
        try:
            login_btn = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_BUTTON))
            login_btn.click()
            
            email_field = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_FORM_EMAIL))
            email_field.clear()
            email_field.send_keys("lyamina_24@gmail.com")
            
            password_field = driver.find_element(*RegistrationPageLocators.LOGIN_FORM_PASSWORD)
            password_field.clear()
            password_field.send_keys("!QAZ2wsx")
            
            driver.find_element(*RegistrationPageLocators.LOGIN_SUBMIT_BUTTON).click()
            wait.until(EC.visibility_of_element_located(RegistrationPageLocators.USER_AVATAR))
        except Exception as e:
            pytest.fail(f"Ошибка авторизации: {str(e)}")
            return

        try:
            create_ad_btn = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.CREATE_AD_BUTTON))
            create_ad_btn.click()
        except Exception as e:
            pytest.fail(f"Не удалось перейти к созданию объявления: {str(e)}")
            return

        try:
            title_field = wait.until(EC.visibility_of_element_located(AdCreationLocators.TITLE_FIELD))
            title_field.send_keys("Тестовое объявление")
            
            price_field = wait.until(EC.visibility_of_element_located(AdCreationLocators.PRICE_FIELD))
            price_field.send_keys("1000")
            
            condition_new = wait.until(EC.presence_of_element_located(AdCreationLocators.CONDITION_NEW))
            driver.execute_script("arguments[0].click();", condition_new)
            
            publish_btn = wait.until(EC.element_to_be_clickable(AdCreationLocators.PUBLISH_BUTTON))
            publish_btn.click()
            time.sleep(3)  
        except Exception as e:
            pytest.fail(f"Ошибка при заполнении формы: {str(e)}")
            return

        try:
            avatar = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.USER_AVATAR))
            avatar.click()
            
            wait.until(EC.visibility_of_element_located(AdCreationLocators.MY_ADS_SECTION))
            
            next_buttons = driver.find_elements(*AdCreationLocators.NEXT_PAGE_BUTTON)
            while next_buttons:
                next_buttons[0].click()
                time.sleep(1) 
                next_buttons = driver.find_elements(*AdCreationLocators.NEXT_PAGE_BUTTON)
            
            last_page_ads = driver.find_elements(*AdCreationLocators.FIRST_AD_IN_LIST)
            if not last_page_ads:
                pytest.fail("Нет объявлений в профиле")
            
            last_ad = last_page_ads[-1]
            ad_text = last_ad.text
            
            assert "Тестовое объявление" in ad_text, "Объявление не найдено в профиле"
        except Exception as e:
            pytest.fail(f"Ошибка при проверке объявления: {str(e)}")
            return

