import datetime
import calendar


def meetup_date(year, month):
    c = calendar.monthcalendar(year, month)
    first_week, fourth_week, fifth_week = c[0], c[3], c[4]
    if first_week[calendar.THURSDAY]:
        fourth_thursday = fourth_week[calendar.THURSDAY]
    else:
        fourth_thursday = fifth_week[calendar.THURSDAY]
    return datetime.date(year, month, fourth_thursday)

