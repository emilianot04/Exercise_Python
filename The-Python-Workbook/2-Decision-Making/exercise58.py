""" 
Most years have 365 days. However, the time required for the Earth to orbit the Sun is actually slightly more than that. As a result, an extra day, February 29, is included in some years to correct for this difference. Such years are referred to as leap years.
The rules for determining whether or not a year is a leap year follow:
• Any year that is divisible by 400 is a leap year.
• Of the remaining years, any year that is divisible by 100 is not a leap year. • Of the remaining years, any year that is divisible by 4 is a leap year.
• All other years are not leap years.
Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year.
"""

year = int(input('Insert year: '))


leap_year = year % 400
leap_year4 = year % 4


if(leap_year==0) or (leap_year4 == 0):
    print('The year ' + str(year) + ' is a leap year')
else:
    print('The year ' + str(year) + ' is not a leap year')