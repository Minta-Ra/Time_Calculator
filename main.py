#!/usr/bin/env python3
"""Simple hello app.

Run with:

    python main.py

Or import `main.main()` from tests.
"""

from calculator import calc_monthly_time, calc_monthly_and_yearly_time, calc_yearly_time




# def main():
#     """Main entry used by tests — only prints the hello message.

#     Tests import and call main(), so keep its output minimal and predictable.
#     """
#     print("Hello, World!")


# def calc_monthly_yearly_time(minutes_per_day):
#     hours, minutes = calc_monthly_time(minutes_per_day)
#     print(f"{hours} hours, {minutes} minutes per month")

#     hours, minutes = calc_yearly_time(minutes_per_day)
#     print(f"{hours} hours, {minutes} minutes per year")

if __name__ == "__main__":
    # When run as a script, print the hello message and ask for minutes per day.
    # main()

    # Ask if user wants to input minutes per day or hours per day.
    time_unit = input("Do you want to enter time in (m)inutes or (h)ours? ").lower()  # Normalize input to lowercase for easier comparison.

    if time_unit in ("h", "hour", "hours"):
        # If hours are entered, convert to minutes.
        hours_user_input = input("Enter hours spent per day: ")
        try:
            hours_per_day = int(hours_user_input)
            minutes_per_day = hours_per_day * 60

            calc_monthly_and_yearly_time(minutes_per_day)
 
        except ValueError:
            print("Invalid input: please enter an integer number of hours.")
            exit(1)



    elif time_unit in ("m", "minute", "minutes"):
        # Prompt the user for minutes per day, convert to int and handle invalid input.
        minutes_user_input = input("Enter minutes spent per day: ")
        try:
            minutes_per_day = int(minutes_user_input)
            calc_monthly_and_yearly_time(minutes_per_day)

        except ValueError:
            print("Invalid input: please enter an integer number of minutes.")
            exit(1)
    else:
        print("Invalid input: please enter 'm' for minutes or 'h' for hours.")
        exit(1)
