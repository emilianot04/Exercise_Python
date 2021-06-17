""" 
The length of a month varies from 28 to 31 days. In this exercise you will create a program that reads the name of a month from the user as a string. Then your program should display the number of days in that month. Display “28 or 29 days” for February so that leap years are addressed.
"""

mounth = (input('Insert mounth: '))


if(mounth == 'January' or mounth == 'March' or mounth == 'May'or mounth == 'July' or mounth == 'August' or mounth == 'January' or mounth == 'October' or mounth == 'December'):
    days = '31'
elif(mounth == 'February'):
    days = '28 or 29'
else:
    days = '30'

print('The mounth of ' + mounth + ' have ' + days +' days')

