from selenium.webdriver.common.by import By


class Login:
    textbox_username_xpath = '//*[@id="Email"]'
    textbox_password_xpath = '//*[@id="Password"]'
    button_login_xpath = '//*[@type="submit"]'
    button_logout_xpath = '//*[@id="navbarText"]/ul/li[3]/a'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
