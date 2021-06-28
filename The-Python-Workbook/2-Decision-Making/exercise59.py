""" 
Write a program that reads a date from the user and computes its immediate successor. For example, if the user enters values that represent 2019-11-18 then your program should display a message indicating that the day immediately after 2019-11-18 is 2019-11-19. If the user enters values that represent 2019-11-30 then the program should indicate that the next day is 2019-12-01. If the user enters values that represent 2019-12-31 then the program should indicate that the next day is 2020-01-01. The date will be entered in numeric form with three separate input statements; one for the year, one for the month, and one for the day. Ensure that your program works correctly for leap years.
"""
# user's inputs
year = int(input('Insert year: '))
month = int(input('Insert month: '))
day = int(input('Insert day: '))


if (year % 400 == 0) or (year % 4 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
else:
    leap_year = False


if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


if day < month_length:
    new_day = day+1
else:
    new_day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month = month+1
    
print('Your data is: ' +  str(year) + '-' + str(month) + '-' + str(day))
print('The next date is: ' +  str(year) + '-' + str(month) + '-' + str(new_day))
