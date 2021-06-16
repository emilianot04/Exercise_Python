""" In this exercise, you will create a program that begins by reading a measurement in feet from the user. Then your program should display the equivalent distance in inches, yards and miles. Use the Internet to look up the necessary conversion factors if you don’t have them memorized."""

number_feet = float(input('Insert your feet number: '))
inches = float(number_feet * 12)
yards = float(number_feet / 3)
miles = float(number_feet / 5280)

print('Your feet number is long ' + str(inches) + ' inches, ' + str(yards)+ ' yards, ' + str(miles) + ' miles')