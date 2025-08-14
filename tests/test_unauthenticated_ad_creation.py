import pytest
from locators import RegistrationPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup")
class TestUnauthenticatedAdCreation:
    
    def test_ad_creation_by_unauthenticated_user(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 10)
        
        try:
            create_ad_button = wait.until(
                EC.element_to_be_clickable(RegistrationPageLocators.CREATE_AD_BUTTON))
            create_ad_button.click()
            
            modal_title = wait.until(
                EC.visibility_of_element_located(RegistrationPageLocators.AUTH_MODAL_TITLE))
            
            assert modal_title.is_displayed(), "Заголовок модального окна не отображается"
            assert modal_title.text == "Чтобы разместить объявление, авторизуйтесь", \
                f"Неверный текст заголовка: '{modal_title.text}'"
                        
        except Exception as e:
            pytest.fail(f"Тест завершился с ошибкой: {str(e)}")