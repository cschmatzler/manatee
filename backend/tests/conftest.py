import os


def pytest_runtest_setup(item):
    os.environ["MANATEE_ENV"] = "test"
