def test_check_id_true(bank_app_check_id_true) -> None:
    response = bank_app_check_id_true.check_id()
    assert response is True


def test_check_id_false(bank_app_check_id_false) -> None:
    response = bank_app_check_id_false.check_id()
    assert response is False


def test_time_at_address_true(
        bank_app_check_time_at_address_true) -> None:
    response = bank_app_check_time_at_address_true \
        .check_time_at_address()
    assert response is True


def test_time_at_address_false(
        bank_app_check_time_at_address_false) -> None:
    response = bank_app_check_time_at_address_false \
        .check_time_at_address()
    assert response is False


def test_age_true(bank_app_check_age_true) -> None:
    response = bank_app_check_age_true.check_age()
    assert response is True


def test_age_false(bank_app_check_age_false) -> None:
    response = bank_app_check_age_false.check_age()
    assert response is False
