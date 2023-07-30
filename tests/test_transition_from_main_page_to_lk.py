import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestTransitionToLk:
    def test_transition_to_lk(self, login):
        driver = login
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Сохранить')]")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

'''В этом тесте переходим в ЛК после логина'''