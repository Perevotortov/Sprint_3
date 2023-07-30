from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructor:
    def test_section_filling(self, login):
        driver = login
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Выход')]"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

'''В этом тесте проверяем что после логина в ЛК можно из него выйти'''