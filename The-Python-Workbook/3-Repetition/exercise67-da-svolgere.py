""" 
Write a program that computes the perimeter of a polygon. Begin by reading the x and y coordinates for the first point on the perimeter of the polygon from the user. Then continue reading pairs of values until the user enters a blank line for the x-coordinate. Each time you read an additional coordinate you should compute the distance to the previous point and add it to the perimeter. When a blank line is entered for the x-coordinate your program should add the distance from the last point back to the first point to the perimeter. Then the perimeter should be displayed. Sample input and output values are shown below. The input values entered by the user are shown in bold.
"""
import math

price = float(input('Insert price article(blank to quit): '))
n = 0
sum = 0
if(price == ""):
    print('Value blank is not valid')
else:
    while price != "":
        sum = float(price) + sum
        n = n+1
        price = input('Insert price article(blank to quit): ')

    print('The price of the ' + str(n) + ' article is: ' + str("%.2f" % sum))
    print('The price with card is: ' + str("%.2f" % sum))

rounding_indicator = sum * 100 % 5

if (rounding_indicator < 5 / 2):
    cash_total = sum - rounding_indicator / 100
else:
    cash_total = sum + 0.05 - rounding_indicator / 100

print('The price cash is ' + str("%.2f" % cash_total))
