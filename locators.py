from selenium.webdriver.common.by import By

class MainPage:
    GET_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    BUNS = (By.XPATH, "//h2[contains(text(),'Булки')]") #подраздел кнопки
    BUNS_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div") #кнопка
    SAUSE = (By.XPATH, "//h2[contains(text(),'Соусы')]") #подраздел кнопки
    SAUSE_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]") #кнопка
    FILLINGS = (By.XPATH, "//h2[contains(text(),'Начинки')]") #подраздел кнопки
    FILLINGS_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]") #кнопка
    CABINET_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    LOGO_BUTTON =  (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]") #логотип сайта
    CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDERS_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    ENTER_ACCOUNT = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
class CabinetPage:
    BUTTON_SAVE = (By.XPATH, "//button[contains(text(),'Сохранить')]")
    BUTTON_CANCEL = (By.XPATH, "//button[contains(text(),'Отмена')]")
    BUTTON_EXIT = (By.XPATH, "//button[contains(text(),'Выход')]")

class LoginPage:
    RECOVER_PASSWORD = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    REGISTER_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    LOGIN_FIELD_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_FIELD_EMAIL = (By.XPATH, "//input[@name='name']") #поле логина емейл, только одно поле с name
class RecoverPage:
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    RECOVER_ENTER = (By.XPATH, "//a[contains(text(),'Войти')]")
class RegistrationPage:
    REGISTRATION_ENTER = (By.XPATH, "//a[contains(text(),'Войти')]")
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    REGISTRATION_FIELD_NAME = (By.XPATH, "(//input[@name='name'])[1]") #Поле имени, индекс 1 для точности
    REGISTRATION_FIELD_EMAIL = (By.XPATH, "(//input[@name='name'])[2]") #поле логина емейл, два поля с таким именем поэтому индекс 2
    REGISTRATION_FIELD_PASS = (By.XPATH, "//input[@name='Пароль']")
    REGISTRATION_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")