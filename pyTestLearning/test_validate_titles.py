import pytest

def test_validate_titles():

    expected_title = "google.com"
    actual_title = "Google.com"

    assert actual_title == expected_title , "Titles are not matching"
    assert "googles" in actual_title, "googles does not exists"
    assert False, "forcefully failing the test"
    # run with  --soft-asserts
    # if actual_title==expected_title:
    #     print("test case is passed")
    # else:
    #     print("test case failed")