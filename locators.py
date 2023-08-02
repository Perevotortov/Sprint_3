from selenium.webdriver.common.by import By

class MainPage:
    GET_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    BUNS = (By.XPATH, "//h2[contains(text(),'Булки')]")
    BUNS_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div") #КНОПКА БУЛОК ПЕРЕДЕЛАТЬ!
    SAUSE = (By.XPATH, "//h2[contains(text(),'Соусы')]")
    SAUSE_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]")
    FILLINGS = (By.XPATH, "//h2[contains(text(),'Начинки')]")
    FILLINGS_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]")
    CABINET_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") #заменено
    LOGO_BUTTON =  (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDERS_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    ENTER_ACCOUNT = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]") #заменено
class CabinetPage:
    BUTTON_SAVE = (By.XPATH, "//button[contains(text(),'Сохранить')]")
    BUTTON_CANCEL = (By.XPATH, "//button[contains(text(),'Отмена')]")
    BUTTON_EXIT = (By.XPATH, "//button[contains(text(),'Выход')]")

class LoginPage:
    RECOVER_PASSWORD = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    REGISTER_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
class RecoverPage:
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    RECOVER_ENTER = (By.XPATH, "//a[contains(text(),'Войти')]")
class RegistrationPage:
    REGISTRATION_ENTER = (By.XPATH, "//a[contains(text(),'Войти')]")