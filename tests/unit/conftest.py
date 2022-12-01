import pytest
from bank_app.core import BankApp


@pytest.fixture(scope="class")
def bank_app_check_id_true():
    return BankApp(
        name="Eric Sales De Andrade", dob="01-01-1981", move_in_date="01-01-1999"
    )


@pytest.fixture(scope="class")
def bank_app_check_id_false():
    return BankApp(name=None, dob=None, move_in_date="01-01-1999")


@pytest.fixture(scope="class")
def bank_app_check_time_at_address_true():
    return BankApp(
        name="Eric Sales De Andrade", dob="01-01-1981", move_in_date="01-01-2015"
    )


@pytest.fixture(scope="class")
def bank_app_check_time_at_address_false():
    return BankApp(
        name="Eric Sales De Andrade", dob="01-01-1981", move_in_date="01-01-2022"
    )


@pytest.fixture(scope="class")
def bank_app_check_age_true():
    return BankApp(
        name="Eric Sales De Andrade", dob="01-01-1991", move_in_date="01-01-2022"
    )


@pytest.fixture(scope="class")
def bank_app_check_age_false():
    return BankApp(
        name="Eric Sales De Andrade", dob="01-01-2005", move_in_date="01-01-2022"
    )


@pytest.fixture(scope="class")
def bank_app_check_monthly_income_true():
    return BankApp(
        name="Eric Sales De Andrade",
        dob="01-01-2005",
        move_in_date="01-01-2022",
        monthly_income=3000,
    )


@pytest.fixture(scope="class")
def bank_app_check_monthly_income_false():
    return BankApp(
        name="Eric Sales De Andrade",
        dob="01-01-2005",
        move_in_date="01-01-2022",
        monthly_income=100,
    )


@pytest.fixture(scope="class")
def bank_app_credit_check_true():
    return BankApp(
        name="Eric Sales De Andrade",
        dob="01-01-1988",
        move_in_date="01-01-2001",
        monthly_income=5000,
    )


@pytest.fixture(scope="class")
def bank_app_credit_check_false():
    return BankApp(
        name="Eric Sales De Andrade",
        dob="01-01-1980",
        move_in_date="01-01-2021",  # Less than 3 years residency at current address
        monthly_income=500,
    )  # Low Monthly Income
