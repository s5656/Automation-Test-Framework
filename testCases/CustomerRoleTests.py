import random
import string
import time

import pytest

from pageObject.Login import Login
from utilities.readProperties import ReadConfigFile
from pageObject.AddingCustomer import CustomerRole


def randomGenarator():
    return 'aa'+''.join(random.choices(string.ascii_uppercase + string.digits, k=7))


class Test_003_CustomerRole:
    readconfig = ReadConfigFile()
    baseURL = readconfig.getBaseUrl()
    username = readconfig.getUsername()
    password = readconfig.getPassword()
    name = randomGenarator()
    system_name = randomGenarator()

    @pytest.mark.regression
    def test_addNewCustomer(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        login = Login(self.driver)
        login.setUserName(self.username)
        login.setPassword(self.password)
        login.clickLogin()

        customer_role = CustomerRole(self.driver)
        customer_role.getCustomerMenuTag().openCustomerRole().addNewCustomerRole().addNameOfCustomer(self.name) \
            .freeShopping().taxExempt().overRideDefoultTax().selectTaxType("Including tax") \
            .lifeTimePassword().systemName(self.system_name).saveCustomerRole()

        assert customer_role.getSuccessfulMassage() == "×\nThe new customer role has been added successfully."

        login.clickLogout()
        time.sleep(2)
        self.driver.close()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_modifyUserCustomerRole(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        login = Login(self.driver)
        login.setUserName(self.username)
        login.setPassword(self.password)
        login.clickLogin()

        customer_role = CustomerRole(self.driver)
        customer_role.getCustomerMenuTag().openCustomerRole().editCustomerRole() \
            .addNameOfCustomer(self.name).systemName(self.system_name).saveCustomerRole()

        assert customer_role.getSuccessfulMassage() == "×\nThe customer role has been updated successfully."

        time.sleep(2)
        self.driver.close()

    @pytest.mark.regression
    def test_deleteCustomerRole(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        login = Login(self.driver)
        login.setUserName(self.username)
        login.setPassword(self.password)
        login.clickLogin()

        customer_role = CustomerRole(self.driver)
        customer_role.getCustomerMenuTag().openCustomerRole().editCustomerRole().deleteCustomerRole().acceptDelete()

        assert customer_role.getSuccessfulMassage() == "×\nThe customer role has been deleted successfully."

        time.sleep(2)
        self.driver.close()
