from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage:

    def test_url_correct_from_main_page(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    def test_url_correct_from_cabinet_page(self, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    def test_url_correct_from_recovery_page(self, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    def test_url_correct_from_registration_page(self, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_authorization(self, login):
        driver = login
        wait = WebDriverWait(driver, 2)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        new_button = driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]")
        assert new_button.is_displayed()

    '''Так как все возможные варианты комбинаций ведут на одну страницу с авторизацией, то я сначала проверяю что при 
    переходе по кнопкам текущая ссылка - страница авторизации, а потом отдельно с помощью фикстуры авторизации проверяю
    что можно на этой странице авторизироваться.
    Проверка ввода текста 4 раза займет больше времени чем проверка корректного ввода 1 раз'''
