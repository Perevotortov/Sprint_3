from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import CabinetPage, MainPage


class TestTransitionToMainPage:
    def test_transition_logo_button(self, login):
        driver = login
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((MainPage.GET_ORDER)))
        driver.find_element(*MainPage.CABINET_BUTTON).click()
        wait.until(EC.presence_of_element_located((CabinetPage.BUTTON_SAVE)))
        driver.find_element(*MainPage.LOGO_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transition_constructor_button(self, login):
        driver = login
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((MainPage.GET_ORDER)))
        driver.find_element(*MainPage.CABINET_BUTTON).click()
        wait.until(EC.presence_of_element_located((CabinetPage.BUTTON_SAVE)))
        driver.find_element(*MainPage.CONSTRUCTOR).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

''' В этом тесте логинимся, переходим в ЛК и потом переходим на главную через кнопку лого и кнопку конструктора'''