import pytest
import allure
from pageObject.Login import Login
from utilities.readProperties import ReadConfigFile
from utilities.customLogger import LogGenrator


# pytest gathers tests according to a naming convention.
# By default, any file that is contained tests must be named starting with test_
@allure.severity(allure.severity_level.NORMAL)
class Test_001_Login:
    readconfig = ReadConfigFile()
    baseURL = readconfig.getBaseUrl()
    username = readconfig.getUsername()
    password = readconfig.getPassword()

    logger = LogGenrator.logFileGenrator()  # created object and called method

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********* Test_001_Login **********")
        self.logger.info("**********Home page validation started*********")
        self.driver = setup
        self.driver.get(self.baseURL)

        if self.driver.title == "Your store. Login":
            self.logger.info("**********Home page validation test pass*********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("/Users/testvagrant/PycharmProjects/nopApp/Screenshots/test_homePageTitle.png")
            self.driver.close()
            self.logger.info("**********Home page validation test fail*********")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        login = Login(self.driver)
        login.setUserName(self.username)
        login.setPassword(self.password)
        login.clickLogin()
        actual_title = self.driver.title
        login.clickLogout()

        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("/Users/testvagrant/PycharmProjects/nopApp/Screenshots/test_login.png")
            self.driver.close()
            assert False
