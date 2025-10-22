import pytest

from calc import add,sub,mul,div

def test_add():
    #compare actual o/p and expected o/p
    assert add(2,3) == 5

def test_sub():
    assert sub(4,3) == 1

def test_mul():
    assert mul(2,3) == 6

def test_div():
    assert div(10,2) == 5