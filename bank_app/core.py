from datetime import datetime


def calculate_diff_in_years(
        date_x: str) -> int | float:
    date_x_date = datetime.strptime(date_x, '%d-%m-%Y').date()
    date_difference = (datetime.today().date() - date_x_date)
    duration_in_s = date_difference.total_seconds()
    years = divmod(duration_in_s, 31536000)[0]
    return years


class BankApp:
    """A simple Bank App"""

    def __init__(
            self,
            name: str = None,
            dob: str = None,
            move_in_date: str = None,
            monthly_income: int | float = None) -> None:
        self.name = name
        self.dob = dob
        self.move_in_date = move_in_date
        self.monthly_income = monthly_income

    def check_id(self) -> bool:
        if all(v is not None for v in [self.name,
                                       self.dob,
                                       self.move_in_date]):
            return True
        return False

    def check_time_at_address(self) -> bool:
        years_at_address = calculate_diff_in_years(
            date_x=self.move_in_date)
        if years_at_address >= 3:
            return True
        return False

    def check_age(self) -> bool:
        age = calculate_diff_in_years(
            date_x=self.dob)
        if age >= 18:
            return True
        return False

    def check_monthly_income(self) -> bool:
        if self.monthly_income > 1000:
            return True
        return False

    def credit_check(self) -> dict:
        response = {"Status": "DECLINED"}
        check_id_ = self.check_id()
        check_time_at_address_ = self.check_time_at_address()
        check_age_ = self.check_age()
        check_monthly_income_ = self.check_monthly_income()
        if all(v for v in [check_id_,
                           check_time_at_address_,
                           check_age_,
                           check_monthly_income_]):
            response = {"Status": "APPROVED"}
            return response
        return response
