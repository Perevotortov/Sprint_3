from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestTransitionToMainPage:
    def test_transition_logo_button(self, login):
        driver = login
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Сохранить')]")))
        #кнопка логотипа
        driver.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transition_constructor_button(self, login):
        driver = login
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Сохранить')]")))
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

''' В этом тесте логинимся, переходим в ЛК и потом переходим на главную через кнопку лого и кнопку конструктора'''