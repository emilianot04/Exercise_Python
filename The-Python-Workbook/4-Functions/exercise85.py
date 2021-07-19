""" Write a function that takes the lengths of the two shorter sides of a right triangle as its parameters. Return the hypotenuse of the triangle, computed using Pythagorean theorem, as the function’s result. Include a main program that reads the lengths of the shorter sides of a right triangle from the user, uses your function to compute the length of the hypotenuse, and displays the result. """

import math


def hypotenuse():
    a = float(input('Insert side a:'))
    b = float(input('Insert side b:'))
    c = math.sqrt((a**2) + (b**2))
    print('The side c is :', float(c))


hypotenuse()
