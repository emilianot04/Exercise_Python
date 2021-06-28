""" 
The following formula can be used to determine the day of the week for January 1
in a given year:
day_of_the_week = (year + floor((year − 1) / 4) − floor((year − 1) / 100) + floor((year − 1) / 400)) % 7

The result calculated by this formula is an integer that represents the day of the week. Sunday is represented by 0. The remaining days of the week following in sequence through to Saturday, which is represented by 6.
Use the formula above to write a program that reads a year from the user and reports the day of the week for January 1 of that year. The output from your program should include the full name of the day of the week, not just the integer returned by the formula.

"""
# user's inputs
year = int(input('Insert year: '))

day_of_the_week = (year + int((year - 1) / 4) - int((year - 1) / 100) + int((year - 1) / 400)) % 7

if(day_of_the_week == 0):
    day = '1 January ' + str(year) + ' is Sunday'
elif(day_of_the_week == 1):
    day = '1 January ' + str(year) + ' is Monday'  
elif(day_of_the_week == 2):
    day = '1 January ' + str(year) + ' is Tuesday'  
elif(day_of_the_week == 3):
    day = '1 January ' + str(year) + ' is Wednesday'  
elif(day_of_the_week == 4):
    day = '1 January ' + str(year) + ' is Thursday'  
elif(day_of_the_week == 5):
    day = '1 January ' + str(year) + ' is Friday'  
elif(day_of_the_week == 6):
    day = '1 January ' + str(year) + ' is Saturday'


print(day)

