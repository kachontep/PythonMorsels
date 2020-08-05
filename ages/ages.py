import re
from datetime import datetime
from fractions import Fraction
from typing import Optional

__all__ = ["get_age", "is_over"]

BORN_DATE_FORMAT = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def get_age(birth_date_string: str, exact: Optional[bool] = False) -> int:
    if exact:
        return Fraction(
            get_day_duration(date_from_string(birth_date_string), datetime.today()), 365
        )
    else:
        return get_year_duration(date_from_string(birth_date_string), datetime.today())


def is_over(age: int, birth_date_string: str) -> bool:
    return (
        get_year_duration(date_from_string(birth_date_string), datetime.today()) >= age
    )


def get_day_duration(since_date: datetime, to_date: datetime) -> int:
    return (to_date - since_date).days


def get_year_duration(since_date: datetime, to_date: datetime) -> int:
    result_duration = to_date.year - since_date.year
    today_in_birth = date_in_birth_year(since_date.year, to_date)
    if today_in_birth < since_date:
        result_duration -= 1
    return result_duration


def date_from_string(birth_date_string):
    match = BORN_DATE_FORMAT.search(birth_date_string)
    if not match:
        raise ValueError(
            "Invalid born date format, the correct on should be in YYYY-mm-dd"
        )
    year, month, day = match.groups()
    birth_date = datetime(int(year), int(month), int(day))
    return birth_date


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0)


def date_in_birth_year(birth_year, day):
    tb_year, tb_month, tb_day = birth_year, day.month, day.day
    if not is_leap_year(tb_year) and (tb_month == 2 and tb_day == 29):
        tb_day = 28  # Round down to 28 Feb
    today_in_birth = datetime(tb_year, tb_month, tb_day)
    return today_in_birth
