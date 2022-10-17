from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.dropdown_sign = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
        self.logout = "Logout"

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.dropdown_sign).click()
        self.driver.find_element(By.LINK_TEXT, self.logout).click()