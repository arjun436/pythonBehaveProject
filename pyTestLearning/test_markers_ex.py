import pytest


@pytest.mark.functional
def test_login():
    print("Executing login test")


@pytest.mark.regression
def test_user_reg():
    print("Executing login test")


@pytest.mark.functional
def test_compose_email():
    print("Executing login test")

    # -s -v -k login or "not login" or -s -v -m functional
    # regester markers in pytest.ini file and run -s -v -m functional or -s -v -m "not functional"

@pytest.mark.skip
def test_skip():
    print("skip test")