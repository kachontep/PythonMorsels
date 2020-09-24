from calendar import week
import datetime
import calendar
from enum import IntEnum


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date_(year, month, nth=4, weekday=3):
    c = calendar.monthcalendar(year, month)

    if nth > 0:
        start_week, nth_week, next_nth_week = (
            c[0],
            c[nth - 1],
            (c[nth] if nth < len(c) else None),
        )
    else:
        start_week, nth_week, next_nth_week = (
            c[-1],
            c[nth],
            (c[nth - 1] if len(c) + nth - 1 >= 0 else None),
        )

    if start_week[weekday]:
        fourth_thursday = nth_week[weekday]
    else:
        fourth_thursday = next_nth_week[weekday]

    return datetime.date(year, month, fourth_thursday)


NUM_DAYS_OF_MONTH = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
]


def number_of_days_in_month(year, month):
    if month == 2 and (year % 4 == 0 and year % 100 == 0 or year % 400 == 0):
        return NUM_DAYS_OF_MONTH[month - 1] + 1
    else:
        return NUM_DAYS_OF_MONTH[month - 1]


def meetup_date(year, month, nth=4, weekday=Weekday.THURSDAY):
    num_of_days = number_of_days_in_month(year, month)
    if nth > 0:
        start = datetime.date(year, month, 1)
        diff = 1
    else:
        start = datetime.date(year, month, num_of_days)
        diff = -1
    days_in_month = [
        start + datetime.timedelta(days=diff * i) for i in range(num_of_days)
    ]
    recurrings = [d for d in days_in_month if d.weekday() == weekday]
    result = recurrings[int(abs(nth)) - 1]
    return result

