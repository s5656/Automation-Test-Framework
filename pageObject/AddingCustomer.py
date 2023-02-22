from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObject.ChooseProduct import ChooseProduct


class CustomerRole:
    customerMenuTag_xpath = '//*[@class="mt-2"]/ul[1]/li[4]/a'
    customerRole_xpath = '//a[@href="/Admin/CustomerRole/List"]/i'
    addNewRole_xpath = '/html/body/div[3]/div[1]/div/div/a'
    editRole_xpath = '//tbody/tr[1]/td[6]/a'
    txtName_xpath = '//*[@id="Name"]'
    checkOnActiveStatus_xpath = '//*[@id="Active"]'
    checkBoxFreeShopping_xpath = '//*[@id="FreeShipping"]'
    checkBoxTax_xpath = '//*[@id="TaxExempt"]'
    checkBoxOverrideTax_xpath = '//*[@id="OverrideTaxDisplayType"]'
    selectTaxType_xpath = '//*[@id="DefaultTaxDisplayTypeId"]'  # Including tax, #Excluding tax
    checkBoxLifeTimePassword_xpath = '//*[@id="EnablePasswordLifetime"]'
    chooseProduct_xpath = '//div[@class="col-md-9"]//button[1]'
    removeProduct_xpath = '//*[@id="purchased-with-product-name-remove"]'
    systemName_xpath = '//*[@id="SystemName"]'
    saveButton_xpath = '//button[@name="save"]'
    saveAndContinueButton_xpath = '//button[@name="save-continue"]'
    deleteButton_xpath = '//*[@id="customerrole-delete"]'

    deleteAccept_xpath = '//*[@id="customerrolemodel-Delete-delete-confirmation"]/div/div/form/div/div[2]/button'
    deleteReject_xpath = '//*[@id="customerrolemodel-Delete-delete-confirmation"]/div/div/form/div/div[2]/span'

    successfulMassage_xpath = '/html/body/div[3]/div[1]/div[1]'

    def __init__(self, driver):
        self.driver = driver

    def getCustomerMenuTag(self):
        self.driver.find_element(By.XPATH, self.customerMenuTag_xpath).click()
        return self

    def openCustomerRole(self):
        self.driver.find_element(By.XPATH, self.customerRole_xpath).click()
        return self

    def addNewCustomerRole(self):
        self.driver.find_element(By.XPATH, self.addNewRole_xpath).click()
        return self

    def addNameOfCustomer(self, name):
        self.driver.find_element(By.XPATH, self.txtName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtName_xpath).send_keys(name)
        return self

    def editCustomerRole(self):
        self.driver.find_element(By.XPATH, self.editRole_xpath).click()
        return self

    def freeShopping(self):
        self.driver.find_element(By.XPATH, self.checkBoxFreeShopping_xpath).click()
        return self

    def taxExempt(self):
        self.driver.find_element(By.XPATH, self.checkBoxTax_xpath).click()
        return self

    def overRideDefoultTax(self):
        self.driver.find_element(By.XPATH, self.checkBoxOverrideTax_xpath).click()
        return self

    def selectTaxType(self, types):
        Select(self.driver.find_element(By.XPATH, self.selectTaxType_xpath)).select_by_visible_text(types)
        return self

    def lifeTimePassword(self):
        self.driver.find_element(By.XPATH, self.checkBoxLifeTimePassword_xpath).click()
        return self

    def chooseProduct(self,):
        self.driver.find_element(By.XPATH, self.chooseProduct_xpath).click()
        windowIDs = self.driver.window_handles
        self.driver.switch_to.window(windowIDs[1])
        ChooseProduct(self.driver).selectTheProduct()
        return self

    def systemName(self, nameOfSystem):
        self.driver.find_element(By.XPATH, self.systemName_xpath).clear()
        self.driver.find_element(By.XPATH, self.systemName_xpath).send_keys(nameOfSystem)
        return self

    def saveCustomerRole(self):
        self.driver.find_element(By.XPATH, self.saveButton_xpath).click()
        return self

    def saveAndEditCustomerRole(self):
        self.driver.find_element(By.XPATH, self.saveAndContinueButton_xpath).click()
        return self

    def getSuccessfulMassage(self):
        return self.driver.find_element(By.XPATH, self.successfulMassage_xpath).text

    def deleteCustomerRole(self):
        self.driver.find_element(By.XPATH, self.deleteButton_xpath).click()
        return self

    def acceptDelete(self):
        self.driver.find_element(By.XPATH, self.deleteAccept_xpath).click()


