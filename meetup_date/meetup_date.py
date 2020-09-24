import datetime
import calendar


def meetup_date(year, month, nth=4, weekday=3):
    c = calendar.monthcalendar(year, month)
    first_week, fourth_week, fifth_week = (
        c[0],
        c[nth - 1],
        (c[nth] if nth < len(c) else None),
    )
    if first_week[weekday]:
        fourth_thursday = fourth_week[weekday]
    else:
        fourth_thursday = fifth_week[weekday]
    return datetime.date(year, month, fourth_thursday)

