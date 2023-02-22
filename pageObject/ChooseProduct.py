from selenium.webdriver.common.by import By


class ChooseProduct:
    selectFirstProduct_xpath = '//tbody/tr[1]/td/button[@type="button"]'

    def __init__(self, driver):
        self.driver = driver

    def selectTheProduct(self):
        self.driver.find_element(By.XPATH, self.selectFirstProduct_xpath).click()
