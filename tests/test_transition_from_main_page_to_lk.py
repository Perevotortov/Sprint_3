from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPage, CabinetPage


class TestTransitionToLk:
    def test_transition_to_lk(self, login):
        driver = login
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((MainPage.GET_ORDER)))
        driver.find_element(*MainPage.CABINET_BUTTON).click()
        wait.until(EC.presence_of_element_located((CabinetPage.BUTTON_SAVE)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

'''В этом тесте переходим в ЛК после логина'''