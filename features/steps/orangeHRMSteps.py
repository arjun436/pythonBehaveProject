import os
import subprocess
import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install(), service_args=["--verbose", "--log-path=cd.log"])
#subprocess.Popen(["start","chrome","--remote-debugging-port=9222","--user-data-dir=" "C:\chromedata",],shell=True)

chrome_options = Options()
#chrome_options.add_argument("--headless") # Runs Chrome in headless mode.
chrome_options.add_argument('--no-sandbox') # Bypass OS security model
chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
chrome_options.add_argument('start-maximized') #
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument("--disable-extensions")
#, service_args=["--verbose", "--log-path=cd.log"])
# chrome_options.add_experimental_option("debuggerAddress", "localhost:8181")
# cmd -path to chrome.exe \\>chrome.exe --remote-debugger-port=9222 --user-data-dir="c:\chromedata"

driver = webdriver.Chrome(service=service, options=chrome_options)

@given('launch chrome browser')
def launchBrowser(self):
    #chrome_options = Options()
    #chrome_options.add_argument("--disable-extensions")
    #driver = webdriver.Chrome(executable_path=ChromeDriverManager.install())
    #driver = webdriver.Chrome(service=service)
    print("browser launched")
    driver.maximize_window()


@when('open orange hrm homepage')
def openHomePgae(self):
    driver.get("https://opensource-demo.orangehrmlive.com")
    time.sleep(10)

@then('verify that the logo present on the page')
def verifyLogo(self):
    status = driver.find_element("xpath", "//div[@class='orangehrm-login-branding']//img").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(self):
    #driver.close()
    #driver.quit()
    print("waiting")
