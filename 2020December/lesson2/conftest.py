import pytest
from datetime import datetime


@pytest.fixture(scope="function")
def set_time():
    start_time = datetime.now()
    yield
    finish_time = datetime.now()
    print("\ntest execution time: ", finish_time - start_time)


@pytest.fixture(scope="session")
def set_time_session():
    start_time = datetime.now()
    yield
    finish_time = datetime.now()
    print("\ntest execution time: ", finish_time - start_time)


@pytest.fixture(params=(1, 2, 3, 4, 5))
def start_num(request, stop_num):
    print("\n this is request: ", request.param)
    print("\n this is stop_num: ", stop_num)
    return request.param, stop_num


@pytest.fixture(params=(10, 20, 30, 40, 50))
def stop_num(request):
    return request.param


def pytest_html_report_title(report):
    report.title = "My very own title!"
