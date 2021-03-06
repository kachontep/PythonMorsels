import re
from datetime import datetime
from fractions import Fraction
from typing import Optional

__all__ = ["get_age", "is_over"]

BORN_DATE_FORMAT = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def get_age(birth_date_string: str, exact: Optional[bool] = False) -> int:
    today = datetime.today()
    if exact:
        days_in_year = get_days_in_year(today.year)
        return Fraction(
            get_day_duration(date_from_string(birth_date_string), today, days_in_year),
            days_in_year,
        )
    else:
        return get_year_duration(date_from_string(birth_date_string), today)


def get_days_in_year(year):
    return is_leap_year(year) and 366 or 365


def is_over(age: int, birth_date_string: str) -> bool:
    return (
        get_year_duration(date_from_string(birth_date_string), datetime.today()) >= age
    )


def get_day_duration(since_date: datetime, to_date: datetime, days_in_year: int) -> int:
    if since_date > to_date:
        since_date, to_date = to_date, since_date
    if since_date.year == to_date.year:
        return (to_date - since_date).days
    first_year_days = (datetime(since_date.year, 12, 31) - since_date).days
    last_year_days = (to_date - datetime(to_date.year - 1, 12, 31)).days
    interim_year_days = (to_date.year - since_date.year - 1) * days_in_year
    return first_year_days + interim_year_days + last_year_days


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
    return (year % 4 == 0) and ((year % 100 == 0 and year % 400 == 0) or year % 100 > 0)


def date_in_birth_year(birth_year, day):
    tb_year, tb_month, tb_day = birth_year, day.month, day.day
    if not is_leap_year(tb_year) and (tb_month == 2 and tb_day == 29):
        tb_day = 28  # Round down to 28 Feb
    today_in_birth = datetime(tb_year, tb_month, tb_day)
    return today_in_birth
