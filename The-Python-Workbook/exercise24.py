""" 
Create a program that reads a duration from the user as a number of days, hours, minutes, and seconds. Compute and display the total number of seconds represented
by this duration.

"""

days = int(input('Insert days: '))
hours = int(input('Insert hours: '))
minutes = int(input('Insert minutes: '))
seconds = int(input('Insert seconds: '))

days_final = days*24*60*60
hours_final = hours*60*60
minutes_final = minutes*60
seconds_final = days_final + hours_final + minutes_final + seconds

print(days_final, hours_final, minutes_final, seconds)

print('Time in seconds : ' + str(seconds_final))
