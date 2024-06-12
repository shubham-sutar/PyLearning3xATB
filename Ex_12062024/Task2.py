# Task 2

""" 1. Leap Year Checker:
Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination."""

# code for Leap Year Checker:

leap_year = int(input("enter year: "))

if leap_year % 4 == 0:
    print(f"{leap_year} is leap_year")
elif leap_year % 100 == 0:
    print(f"{leap_year} is not leap_year")
elif leap_year % 400 == 0:
    print(f"{leap_year} is leap_year")
else:
    print(f"{leap_year} is not leap_year")













