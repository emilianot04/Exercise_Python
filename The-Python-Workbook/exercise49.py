""" 
The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is shown in the table below. The pattern repeats from there, with 2012 being another year of the dragon, and 1999 being another year of the hare.
Write a program that reads a year with that year. Your program should to zero, not just the ones listed in the table.

"""

year = int(input('Insert year: '))

if year % 12 == 8:
    sign = "Dragon"
elif year % 12 == 9:
    sign = "Snake"
elif year % 12 == 10:
    sign = "Horse"
elif year % 12 == 11:
    sign = "Sheep"
elif year % 12 == 0:
    sign = "Monkey"
elif year % 12 == 1:
    sign = "Rooster"
elif year % 12 == 2:
    sign = "Dog"
elif year % 12 == 3:
    sign = "Pig"
elif year % 12 == 4:
    sign = "Rat"
elif year % 12 == 5:
    sign = "Ox"
elif year % 12 == 6:
    sign = "Tiger"
elif year % 12 == 7:
    sign = "Hare"
print('The sign is ' + sign)
