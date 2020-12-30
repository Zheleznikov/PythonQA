import pytest


@pytest.mark.smoke
@pytest.mark.xfail(reason="cause look at bug ..")
def test_firsts():
    a = 2
    b = 3
    assert a+b == 5
