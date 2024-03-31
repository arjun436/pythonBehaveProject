import pytest

@pytest.fixture(scope='module')
def setup():
    print("creating DB connection")

    yield
    print("closing DB function")

@pytest.fixture(scope='function')
def before():
    print("launching browser")

    yield
    print("closing browser")

# def test_login(setup, before):
#     print("Executing the login test")
#
# def test_user_reg(setup, before):
#     print("Executing the user reg")

@pytest.mark.usefixtures("setup", "before")
def test_login():
    print("Executing the login test")

@pytest.mark.usefixtures("setup", "before")
def test_user_reg():
    print("Executing the user reg")