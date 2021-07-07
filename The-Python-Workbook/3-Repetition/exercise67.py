""" 
Write a program that computes the perimeter of a polygon. Begin by reading the x and y coordinates for the first point on the perimeter of the polygon from the user. Then continue reading pairs of values until the user enters a blank line for the x-coordinate. Each time you read an additional coordinate you should compute the distance to the previous point and add it to the perimeter. When a blank line is entered for the x-coordinate your program should add the distance from the last point back to the first point to the perimeter. Then the perimeter should be displayed. Sample input and output values are shown below. The input values entered by the user are shown in bold.
# Enter the first x-coordinate: 0
# Enter the first y-coordinate: 0
# Enter the next x-coordinate (blank to quit): 1
# Enter the next y-coordinate: 0
# Enter the next x-coordinate (blank to quit): 0
# Enter the next y-coordinate: 1
# Enter the next x-coordinate (blank to quit):
# The perimeter of that polygon is 3.414213562373095  
"""
from math import sqrt

X_coordinate = float(input('Enter the first x-coordinate: '))
Y_coordinate = float(input('Enter the first y-coordinate: '))

prev_x = X_coordinate
prev_y = Y_coordinate
perimeter = 0

X_next_coordinate =input('Enter the next x-coordinate (blank to quit): ')

while X_next_coordinate != "":
    x = float(X_next_coordinate)
    y = float(input('Enter the next y-coordinate: '))
       
    distance = sqrt((prev_x - x) ** 2 + (prev_y - y)**2 )
    perimeter = perimeter + distance

    prev_x = x
    prev_y = y

    X_next_coordinate = input('Enter the next x-coordinate (blank to quit): ')

distance = sqrt((X_coordinate -x)**2 + (Y_coordinate - y)**2 )
perimeter = perimeter + distance

print("The perimeter of that polygon is", str(perimeter))
