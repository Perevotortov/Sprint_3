import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage, LoginPage, RecoverPage, RegistrationPage


class TestLoginPage:

    def test_url_correct_from_main_page(self, driver):
        driver.find_element(*MainPage.ENTER_ACCOUNT).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    def test_url_correct_from_cabinet_page(self, driver):
        driver.find_element(*MainPage.CABINET_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_url_correct_from_recovery_page(self, driver):
        driver.find_element(*MainPage.CABINET_BUTTON).click()
        driver.find_element(*LoginPage.RECOVER_PASSWORD).click()
        time.sleep(1)
        driver.find_element(*RecoverPage.RECOVER_ENTER).click()
        time.sleep(1)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_url_correct_from_registration_page(self, driver):
        driver.find_element(*MainPage.CABINET_BUTTON).click()
        driver.find_element(*LoginPage.REGISTER_BUTTON).click()
        time.sleep(1)
        driver.find_element(*RegistrationPage.REGISTRATION_ENTER).click()
        time.sleep(1)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    def test_authorization(self, login):
        driver = login
        wait = WebDriverWait(driver, 2)
        wait.until(EC.presence_of_element_located(MainPage.GET_ORDER))
        assert driver.find_element(*MainPage.GET_ORDER).is_displayed()

    '''Так как все возможные варианты комбинаций ведут на одну страницу с авторизацией, то я сначала проверяю что при 
    переходе по кнопкам текущая ссылка - страница авторизации, а потом отдельно с помощью фикстуры авторизации проверяю
    что можно на этой странице авторизироваться.
    Проверка ввода текста 4 раза займет больше времени чем проверка корректного ввода 1 раз'''
