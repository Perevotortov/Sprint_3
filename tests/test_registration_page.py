from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPage, LoginPage


class TestRegistrationPage:
    def test_registration(self, registration):
        driver = registration
        wait = WebDriverWait(driver, 2)
        driver.find_element(*RegistrationPage.REGISTRATION_FIELD_PASS).send_keys("Pass12")
        wait.until(EC.presence_of_element_located((RegistrationPage.REGISTRATION_BUTTON))).click()
        wait.until(EC.presence_of_element_located((LoginPage.ENTER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_registration_password_warning(self, registration):
        driver = registration
        wait = WebDriverWait(driver, 2)
        driver.find_element(*RegistrationPage.REGISTRATION_FIELD_PASS).send_keys("Pass")
        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()
        assert wait.until(EC.presence_of_element_located((RegistrationPage.REGISTRATION_ERROR_MESSAGE))).is_displayed

'''В этом тесте проверяем что процесс регистрации проходит успешно, и при некорректном пароле появляется предупрежденеие
В тестах использую фикстуру get_mail для генерации почты'''