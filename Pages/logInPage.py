from selenium.webdriver.common.by import By


class LogIn:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = "//input[@placeholder='Username']"
        self.password_textbox = "//input[@placeholder='Password']"
        self.login_button = "//button[normalize-space()='Login']"
        self.invalid_text = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def get_invalid_text(self):
        msg = self.driver.find_element(By.XPATH, self.invalid_text).text
        return msg