import time
import unittest
from Pages.logInPage import LogIn
from Pages.homePage import HomePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class LogInLogOut(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # cls.s = Service("C:\\Users\\Mim\\PycharmProjects\\orangePomPythonSeleniumProject\\chromedriver.exe")
        # cls.driver = webdriver.Chrome(service=cls.s)

    def test_01_logValidTest(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()

        login = LogIn(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login_button()

        logout = HomePage(driver)
        logout.click_logout()
        time.sleep(4)

    def test_02_logInValidTest(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()

        login = LogIn(driver)
        login.enter_username("Admin123")
        login.enter_password("admin123")
        login.click_login_button()
        actual_text = login.get_invalid_text()
        expected_text = "Invalid credentials"
        self.assertEqual(actual_text, expected_text)
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
