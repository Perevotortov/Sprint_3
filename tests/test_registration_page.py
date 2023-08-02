import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestRegistrationPage:
    def test_registration(self, registration):
        driver = registration
        wait = WebDriverWait(driver, 2)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("Pass12")
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_registration_password_warning(self, registration):
        driver = registration
        wait = WebDriverWait(driver, 2)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("Pass")
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Некорректный пароль')]")))
        error_message = driver.find_element(By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
        assert error_message.is_displayed()

'''В этом тесте проверяем что процесс регистрации проходит успешно, и при некорректном пароле появляется предупрежденеие
В тестах использую фикстуру get_mail для генерации почты'''