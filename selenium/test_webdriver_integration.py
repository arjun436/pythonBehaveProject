import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def log_on_failure(request, get_browser):
    driver = get_browser
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name='failed', attachment_type=AttachmentType.PNG)


def get_data():
    return [
        ("arjun.miryala@gmail.com", "asdasdasds"),
        ("chirru.miryala@gmail.com", "gdgd"),
        ("andwit.miryala@gmail.com", "asdetr"),
    ]

@pytest.fixture()
def teardown_function(get_browser):
    driver = get_browser
    driver.close()
    driver.quit()


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username, password", get_data())
def test_dologin(username, password, get_browser):
    driver = get_browser
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    assert 1 == 2
    # allure.attach(driver.get_screenshot_as_png(), name='dologin',attachment_type=AttachmentType.PNG)

# run parallel mode install pip install pytest-xdist or add addopts = -n3 in pytest.ini file
# run the test with  pytest test_webdriver_integration.py -n 3 where 3 is nuber of parallel tests
# run  pytest test_webdriver_integration.py -n 3 --alluredir="./allurereports" to generate allure json
# run allure serve ./allurereports
