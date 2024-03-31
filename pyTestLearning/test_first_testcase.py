import pytest

def setup_module(module):
    print("creating DB connection")

def teardown_module(module):
    print("closing DB connection")

def setup_function(function):
    print("launching browser")

def teardown_function(function):
    print("quitting the browser")

def test_login():
    print("Executing the login test")

def test_user_reg():
    print("Executing the user reg")