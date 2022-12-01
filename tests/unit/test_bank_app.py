def test_check_id_true(bank_app_check_id_true) -> None:
    """
    Test to check if ID is True
    :param bank_app_check_id_true:
        Fixture (defined in conftest.py)
    :return: None
    """
    response = bank_app_check_id_true.check_id()
    assert response is True


def test_check_id_false(bank_app_check_id_false) -> None:
    """
    Test to check if ID is False
    :param bank_app_check_id_false:
        Fixture (defined in conftest.py)
    :return: None
    """
    response = bank_app_check_id_false.check_id()
    assert response is False


def test_time_at_address_true(bank_app_check_time_at_address_true) -> None:
    """
    Test to check if time at address is True
    :param bank_app_check_time_at_address_true:
        Fixture (defined in conftest.py)
    :return: None
    """
    response = bank_app_check_time_at_address_true.check_time_at_address()
    assert response is True


def test_time_at_address_false(bank_app_check_time_at_address_false) -> None:
    """
    Test to check if time at address is False
    :param bank_app_check_time_at_address_false:
        Fixture (defined in conftest.py)
    :return: None
    """
    response = bank_app_check_time_at_address_false.check_time_at_address()
    assert response is False


def test_age_true(bank_app_check_age_true) -> None:
    """
    Test to check if age >= 18 condition is True
    :param bank_app_check_age_true:
        Fixture (defined in conftest.py)
    :return: None
    """
    response = bank_app_check_age_true.check_age()
    assert response is True


def test_age_false(bank_app_check_age_false) -> None:
    """
    Test to check if age >= 18 condition is False
    :param bank_app_check_age_false:
        Fixture (defined in conftest.py)
    :return: None
    """
    response = bank_app_check_age_false.check_age()
    assert response is False


def test_monthly_income_true(bank_app_check_monthly_income_true) -> None:
    """
    Test to check if monthly income >= 1000 condition is True
    :param bank_app_check_monthly_income_true:
        Fixture (defined in conftest.py)
    :return: None
    """
    response = bank_app_check_monthly_income_true.check_monthly_income()
    assert response is True


def test_monthly_income_false(bank_app_check_monthly_income_false) -> None:
    """
    Test to check if monthly income >= 1000 condition is False
    :param bank_app_check_monthly_income_false:
        Fixture (defined in conftest.py)
    :return: None
    """
    response = bank_app_check_monthly_income_false.check_monthly_income()
    assert response is False


def test_credit_check_approved(bank_app_credit_check_true) -> None:
    """
    Test to check if credit check is APPROVED
    :param bank_app_credit_check_true:
        Fixture (defined in conftest.py)
    :return: None
    """
    response = bank_app_credit_check_true.credit_check()
    assert response == {"Status": "APPROVED"}


def test_credit_check_declined(bank_app_credit_check_false) -> None:
    """
    Test to check if credit check is DECLINED
    :param bank_app_credit_check_false:
        Fixture (defined in conftest.py)
    :return: None
    """
    response = bank_app_credit_check_false.credit_check()
    assert response == {"Status": "DECLINED"}
