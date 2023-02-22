import pytest

from pageObject.Login import Login
from utilities.readProperties import ReadConfigFile
from utilities.customLogger import LogGenrator
from utilities import excelUtilities


# pytest gathers tests according to a naming convention.
# By default, any file that is contained tests must be named starting with test_

class Test_002_Login:
    readconfig = ReadConfigFile()
    baseURL = readconfig.getBaseUrl()
    path = '/Users/testvagrant/PycharmProjects/nopApp/TestData/LoginData.xlsx'

    logger = LogGenrator.logFileGenrator()  # created object and called method

    @pytest.mark.regression
    def test_data_driven_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        login = Login(self.driver)

        list_of_expected_result = []
        rows = excelUtilities.getRowCount(self.path, "Sheet1")

        for row in range(2, rows + 1):
            self.username = excelUtilities.readData(self.path, "Sheet1", row, 1)
            self.password = excelUtilities.readData(self.path, "Sheet1", row, 2)
            self.expectedResult = excelUtilities.readData(self.path, "Sheet1", row, 3)

            login.setUserName(self.username)
            login.setPassword(self.password)
            login.clickLogin()
            actual_title = self.driver.title

            if actual_title == "Dashboard / nopCommerce administration":
                if self.expectedResult == "pass":
                    login.clickLogout()
                    list_of_expected_result.append("pass")
                else:
                    list_of_expected_result.append("fail")
            else:
                if self.expectedResult == "fail":
                    list_of_expected_result.append("pass")
                else:
                    list_of_expected_result.append("fail")

        assert "fail" not in list_of_expected_result

        self.driver.quit()
