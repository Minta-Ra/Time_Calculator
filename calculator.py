from datetime import datetime
import calendar


"""Small calculator helpers.

This module contains time calculation helpers extracted from `main.py`.
"""

def calc_monthly_time(minutes_per_day):
    """Calculate the total time spent on some activity in a month.

    Args:
        minutes_per_day (int): number of minutes spent per day.

    Returns:
        tuple: (hours, minutes) total for a 30-day month.
    """
    days_per_month = determine_days_per_current_month()
    total_minutes = minutes_per_day * days_per_month
    return calc_time(total_minutes)

def determine_days_per_current_month():
    """Determine the number of days in the current month.

    Returns:
        int: number of days in the current month.
    """
    now = datetime.now()
    # Use calendar.monthrange(year, month) which returns (weekday_of_first_day, days_in_month)
    return calendar.monthrange(now.year, now.month)[1]

def calc_yearly_time(minutes_per_day):
    """Calculate the total time spent on some activity in a year.

    Args:
        minutes_per_day (int): number of minutes spent per day.

    Returns:
        tuple: (hours, minutes) total for a 365-day year.
    """
    days_per_year = determine_days_per_current_year()
    total_minutes = minutes_per_day * days_per_year
    return calc_time(total_minutes)


def determine_days_per_current_year():
    """Determine the number of days in the current year.

    Returns:
        int: 366 if it's a leap year, otherwise 365.
    """

    current_year = datetime.now().year
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        return 366  # Leap year
    else:
        return 365


def calc_time(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes


def calc_monthly_and_yearly_time(minutes_per_day):
    hours, minutes = calc_monthly_time(minutes_per_day)
    print(f"{hours} hours, {minutes} minutes per month")

    hours, minutes = calc_yearly_time(minutes_per_day)
    print(f"{hours} hours, {minutes} minutes per year")