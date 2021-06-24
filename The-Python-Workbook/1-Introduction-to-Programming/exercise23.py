""" 
A polygon is regular if its sides are all the same length and the angles between all of the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:
Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.
"""

import math
s = float(input('Insert length side: '))
n = float(input('Insert number of side: '))

area = ((n*(s**2)))/(4*math.tan(math.pi/n))

print('The area of the polygon is : ' + '%.2f' % area)
