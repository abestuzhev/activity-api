from datetime import datetime


def format_date(date):
    if isinstance(date, str):
        return datetime.strptime(date, "%d.%m.%Y %H:%M")
    else:
        return date.strftime("%d.%m.%Y %H:%M")

