import pytest


@pytest.mark.regress
@pytest.mark.usefixtures("set_time", "set_time_session")
@pytest.mark.parametrize("test_a, test_b", [(1, 2), (2, 3), (4, 1)])
def test_firsts(test_a, test_b, start_num):
    assert (test_a + test_b) * 10 == start_num[0] * start_num[1]
