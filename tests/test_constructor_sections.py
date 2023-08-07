from locators import MainPage


class TestConstructor:
    def test_section_filling(self, driver):
        driver.find_element(*MainPage.FILLINGS).click()
        assert driver.find_element(*MainPage.FILLINGS).is_displayed()

    def test_section_sauce(self, driver):
        driver.find_element(*MainPage.SAUSE_BUTTON).click()
        assert driver.find_element(*MainPage.SAUSE).is_displayed()

    def test_section_bun(self, driver):
        driver.find_element(*MainPage.SAUSE_BUTTON).click()
        driver.find_element(*MainPage.BUNS_BUTTON).click()
        assert driver.find_element(*MainPage.BUNS).is_displayed()

'''Проверяем переход на кнопку Нвачинки (что фокус переместился на раздел), потом на соусы и булочки'''