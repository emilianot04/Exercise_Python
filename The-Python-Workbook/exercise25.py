""" 
In this exercise you will reverse the process described in Exercise 24. Develop a program that begins by reading a number of seconds from the user. Then your program should display the equivalent amount of time in the form D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours, minutes and seconds should all be formatted so that they occupy exactly two digits. Use your research skills determine what additional character needs to be included in the format specifier so that leading zeros are used instead of leading spaces when a
number is formatted to a particular width.

"""

seconds = int(input('Insert seconds: '))

days_final = seconds//(24*60*60)
days_rest = seconds % (24*60*60)

hours_final = days_rest//(60*60)
hours_rest = days_rest % (60*60)

minutes_final = hours_rest // 60
minutes_rest = hours_rest % 60

seconds_final = days_final + hours_final + minutes_final + minutes_rest

""" print(days_final, hours_final, minutes_final, minutes_rest) """

print(str(days_final) + ':' + str(hours_final) + ':' +
      str(minutes_final) + ':' + str(minutes_rest))
