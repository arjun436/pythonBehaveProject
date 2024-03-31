import pytest

def get_data():

    return [
        ("arjun.miryala@gmail.com","asdasdasds"),
        ("chirru.miryala@gmail.com", "gdgd"),
        ("andwit.miryala@gmail.com", "asdetr"),
    ]

@pytest.mark.parametrize("username, password", get_data())
def test_dologin(username, password):
    print(username,"---",password)