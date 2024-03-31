import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=["chrome", "edge"], scope="function")
def get_browser(request):
    if request.param == "chrome":
        service = Service(executable_path=ChromeDriverManager().install(),
                          service_args=["--verbose", "--log-path=cd.log"])
        chrome_options = Options()
        # chrome_options.add_argument("--headless") # Runs Chrome in headless mode.
        chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
        chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
        chrome_options.add_argument('start-maximized')  #
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(service=service, options=chrome_options)
    if request.param == "edge":
        service = Service(executable_path=EdgeChromiumDriverManager().install(),
                          service_args=["--verbose", "--log-path=cd.log"])
        driver = webdriver.Edge(service=service)

    driver.get("http://facebook.com")
    yield driver



