""" 
Canada has three national holidays which fall on the same dates each year.
Write a program that reads a month and day from the user. If the month and day match one of the holidays listed previously then your program should display the holiday’s name. Otherwise your program should indicate that the entered month and day do not correspond to a fixed-date holiday.
Canada has two additional national holidays, Good Friday and Labour Day, whose dates vary from year to year. There are also numerous provincial and territorial holidays, some of which have fixed dates, and some of which have variable dates. We will not consider any of these additional holidays in this exercise.
"""

day = int(input('Insert day: '))
month = input('Insert month: ')

if day==1 and month =='January':
    holiday =  'New Year’s Day'
elif day== 1 and month=='July':
    holiday= 'Canada Day'
elif day== 25 and month=='December':
    holiday = 'Christmas Day' 
else:
    holiday=''
if holiday:
    print('The day ' + str(day) + ' ' + month + ' is ' + holiday)
else:
    print ('The day ' + str(day) + ' ' + month +' do not correspond to a fixed-date holiday')

