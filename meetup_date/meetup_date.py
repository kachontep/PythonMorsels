import datetime
import calendar


def meetup_date(year, month, nth=4, weekday=3):
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

