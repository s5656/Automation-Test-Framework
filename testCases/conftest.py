import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Adding environment in the report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commers'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Sumit'


# Modify environment info to the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
