""" The volume of a cylinder can be computed by multiplying the area of its circular base by its height. Write a program that reads the radius of the cylinder, along with its height, from the user and computes its volume. Display the result rounded to one decimal place.
"""
import math
radius = float(input('Insert radius: '))
height = float(input('Insert height: '))

volume = (radius**2)*math.pi*height

print('Volume of cylinder: ' + '%.1f' % volume + ' cubic meters')


