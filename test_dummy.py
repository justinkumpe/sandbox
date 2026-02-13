"""Dummy test file for pytest"""
from time import sleep

def test_addition():
    """Test simple addition"""
    sleep(5)
    assert 1 + 1 == 2


def test_string_equality():
    """Test string equality"""
    message = "Hello, World!"
    assert message == "Hello, World!"


def test_list_contains():
    """Test list contains element"""
    arr = [1, 2, 3]
    assert 2 in arr


def test_truthy():
    """Test truthy value"""
    assert True is True
