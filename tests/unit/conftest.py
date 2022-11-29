import pytest
from bank_app.core import BankApp


@pytest.fixture(scope="class")
def bank_app_check_id():
    return BankApp(name="Eric Sales De Andrade",
                   dob="01-01-1981",
                   move_in_date="01-01-1999")


@pytest.fixture(scope="class")
def bank_app_check_time_at_address_true():
    return BankApp(name="Eric Sales De Andrade",
                   dob="01-01-1981",
                   move_in_date="01-01-2015")


@pytest.fixture(scope="class")
def bank_app_check_time_at_address_false():
    return BankApp(name="Eric Sales De Andrade",
                   dob="01-01-1981",
                   move_in_date="01-01-2022")


@pytest.fixture(scope="class")
def bank_app_check_age_true():
    return BankApp(name="Eric Sales De Andrade",
                   dob="01-01-1991",
                   move_in_date="01-01-2022")


@pytest.fixture(scope="class")
def bank_app_check_age_false():
    return BankApp(name="Eric Sales De Andrade",
                   dob="01-01-2005",
                   move_in_date="01-01-2022")
