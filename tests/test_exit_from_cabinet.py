from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPage, CabinetPage, LoginPage


class TestExitFromCabinet:
    def test_section_filling(self, login):
        driver = login
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((MainPage.GET_ORDER)))
        driver.find_element(*MainPage.CABINET_BUTTON).click()
        wait.until(EC.presence_of_element_located((CabinetPage.BUTTON_EXIT))).click()
        assert wait.until(EC.presence_of_element_located((LoginPage.ENTER_BUTTON))).is_displayed()

'''В этом тесте проверяем что после логина в ЛК можно из него выйти'''