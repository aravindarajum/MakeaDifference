import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager



# URL = "https://aravindaec.wixsite.com/makeadifference"

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True

@pytest.fixture(scope="class")
def setup(request,browser,url):
    global driver

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(), desired_capabilities=capabilities))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.maximize_window()
    driver.get(url)

    request.cls.driver = driver

    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")
    # parser.addoption("--browser", action="store", default="chrome",
    #                  help="Browser to run tests on (chrome, firefox, edge)")
    # parser.addoption("--url", action="store", default="https://aravindaec.wixsite.com/makeadifference",
    #                  help="URL of the web application")


@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class",autouse=True)
def url(request):
    return request.config.getoption("--url")

