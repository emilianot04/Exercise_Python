""" 
The year is divided into four seasons: spring, summer, fall (or autumn) and winter. While the exact dates that the seasons change vary a little bit from year to year because of the way that the calendar is constructed, we will use the following dates for this exercise:

Create a program that reads a month and day from the user. The user will enter the name of the month as a string, followed by the day within the month as an integer. Then your program should display the season associated with the date that was entered.

"""

day = int(input('Insert day (from 1 to 31): '))
month = input('Insert month: ')

""" Spring Summer Fall Winter
First Day
March 20 June 21 September 22 December 21 """

if(day >= 1 and day <= 31) and (month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June' or month == 'July' or month == 'August' or month == 'September' or month == 'October' or month == 'November' or month == 'December'):
    if ((day >= 20 and day <= 31) and (month == 'March')) or ((month == 'April' or month == 'May') and (day >= 1 and day <= 31)) or ((day >= 1 and day <= 20) and (month == 'June')):
        season = 'Spring'
    elif((day >= 21 and day <= 31) and (month == 'June')) or ((month == 'July' or month == 'August') and (day >= 1 and day <= 31)) or ((day >= 1 and day <= 21) and (month == 'September')):
        season = 'Summer'
    elif((day >= 22 and day <= 31) and (month == 'September')) or ((month == 'October' or month == 'November') and (day >= 1 and day <= 31)) or ((day >= 1 and day <= 20) and (month == 'December')):
        season = 'Fall'
    elif((day >= 21 and day <= 31) and (month == 'December')) or ((month == 'January' or month == 'February') and (day >= 1 and day <= 31)) or ((day >= 1 and day <= 19) and (month == 'March')):
        season = 'Winter'
    print(season)
else:
    print('Value not valid')
