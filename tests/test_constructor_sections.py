from selenium.webdriver.common.by import By

class TestConstructor:
    def test_section_filling(self, driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()
        assert driver.find_element(By.XPATH, "//h2[contains(text(),'Начинки')]").is_displayed()

    def test_section_sauce(self, driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        assert driver.find_element(By.XPATH, "//h2[contains(text(),'Соусы')]").is_displayed()

    def test_section_bun(self, driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        #кнопка булки
        driver.find_element(By.XPATH, "//section/div/div").click()
        assert driver.find_element(By.XPATH, "//h2[contains(text(),'Булки')]").is_displayed()

'''Проверяем переход на кнопку Нвачинки (что фокус переместился на раздел), потом на соусы и булочки'''