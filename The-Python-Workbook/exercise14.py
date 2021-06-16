""" Many people think about their height in feet and inches, even in some countries that primarily use the metric system. Write a program that reads a number of feet from the user, followed by a number of inches. Once these values are read, your program should compute and display the equivalent number of centimeters. 
Hint: One foot is 12 inches. One inch is 2.54 centimeters."""

number_feet = float(input('Insert your feet number: '))
inches = float(number_feet * 12)
centimeters = float(inches * 2.54)

print('Your feet number is long ' + str(centimeters) + 'cm')