import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import get_mail
from locators import MainPage


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()


@pytest.fixture
def registration(driver):
    driver.find_element(*MainPage.ENTER_ACCOUNT).click()
    driver.find_element(By.XPATH, " // a[contains(text(), 'Зарегистрироваться')]").click()
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Кирилл")
    driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(get_mail())
    return driver

@pytest.fixture
def login(driver):
    email = 'kirillprovotorov@mail.ru'
    password = 'Pass12'
    wait = WebDriverWait(driver, 3)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"))).click()
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    return driver