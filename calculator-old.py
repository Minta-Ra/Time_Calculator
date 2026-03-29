from datetime import datetime
import calendar


"""Small calculator helpers.

This module contains time calculation helpers extracted from `main.py`.
"""

def calc_monthly_duration(minutes_per_day):
    # Compute total minutes for the current month, then break down into days/hours/minutes
    days_in_month = determine_days_per_current_month()
    month_total_minutes = minutes_per_day * days_in_month
    m_days_total = month_total_minutes // (60 * 24)  # total whole days in the month
    m_weeks = m_days_total // 7
    m_rem_days = m_days_total % 7
    m_hours = (month_total_minutes % (60 * 24)) // 60
    m_minutes = month_total_minutes % 60
    m_total_hours = month_total_minutes // 60
    return m_weeks, m_rem_days, m_hours, m_minutes, m_total_hours

def determine_days_per_current_month():
    """Determine the number of days in the current month.

    Returns:
        int: number of days in the current month.
    """
    now = datetime.now()
    # Use calendar.monthrange(year, month) which returns (weekday_of_first_day, days_in_month)
    return calendar.monthrange(now.year, now.month)[1]

def calc_yearly_duration(minutes_per_day):
    # Compute total minutes for the current year, then break down into months/days/hours/minutes
    days_in_year = determine_days_per_current_year()
    year_total_minutes = minutes_per_day * days_in_year
    y_days_total = year_total_minutes // (60 * 24)
    y_weeks = y_days_total // 7
    y_rem_days = y_days_total % 7
    y_months = y_days_total // 30
    y_hours = (year_total_minutes % (60 * 24)) // 60
    y_minutes = year_total_minutes % 60
    y_total_hours = year_total_minutes // 60
    return y_months, y_weeks, y_rem_days, y_hours, y_minutes, y_total_hours

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

def get_time_breakdown(minutes_per_day):
    # Unpack monthly results: (weeks, remaining_days, hours, minutes, total_hours)
    m_weeks, m_rem_days, m_hours, m_minutes, m_total_hours = calc_monthly_duration(minutes_per_day)
    print(f"In total time spent per month: {m_weeks} week(s), {m_rem_days} day(s), {m_hours} hour(s), {m_minutes} minute(s). ({m_total_hours} hour(s))")

    # Unpack yearly results: (months, weeks, remaining_days, hours, minutes, total_hours)
    y_months, y_weeks, y_rem_days, y_hours, y_minutes, y_total_hours = calc_yearly_duration(minutes_per_day)
    print(f"In total time spent per year: {y_months} month(s), {y_weeks} week(s), {y_rem_days} day(s), {y_hours} hour(s), {y_minutes} minute(s). ({y_total_hours} hour(s))")
