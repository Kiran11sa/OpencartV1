import os
from datetime import datetime

import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser='chrome'):
    if browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_argument("start-maximized")
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("start-maximized")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        print("Launching firefox browser.........")
    else:
        options = webdriver.ChromeOptions()
        # driver=options.capabilities['Chrome']
        # driver=webdriver.Chrome()
        # driver = webdriver.Chrome(executable_path='C:/Users/LENOVO/PycharmProjects/OpencartV1/venv/Scripts/chromedriver.exe', options=options)
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("Launching chrome browser.........")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html"

# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture()
# def setup():
#     # driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver = webdriver.Chrome()
#     return driver
