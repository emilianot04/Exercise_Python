""" 
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All three sides of an equilateral triangle have the same length. An isosceles triangle has two sides that are the same length, and a third side that is a different length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of the three sides of a triangle from the user. Then display a message that states the triangle’s type.

"""

side_one = float(input('Insert first side: '))
side_two = float(input('Insert second side: '))
side_three = float(input('Insert third side: '))

if(side_one == side_two == side_three):
    triangle = 'equilater'
elif(side_one != side_two != side_three):
    triangle = 'scalene'
else:
    triangle = 'isosceles'

print('The triangle is ' + triangle)
