import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import get_mail
from locators import MainPage, RegistrationPage, LoginPage


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()


@pytest.fixture
def registration(driver):
    driver.find_element(*MainPage.ENTER_ACCOUNT).click()
    driver.find_element(*LoginPage.REGISTER_BUTTON).click()
    driver.find_element(*RegistrationPage.REGISTRATION_FIELD_NAME).send_keys("Кирилл")
    driver.find_element(*RegistrationPage.REGISTRATION_FIELD_EMAIL).send_keys(get_mail())
    return driver

@pytest.fixture
def login(driver):
    email = 'kirillprovotorov@mail.ru'
    password = 'Pass12'
    wait = WebDriverWait(driver, 3)
    wait.until(EC.presence_of_element_located((MainPage.ENTER_ACCOUNT))).click()
    driver.find_element(*LoginPage.LOGIN_FIELD_PASSWORD).send_keys(password)
    driver.find_element(*LoginPage.LOGIN_FIELD_EMAIL).send_keys(email)
    driver.find_element(*LoginPage.ENTER_BUTTON).click()
    return driver