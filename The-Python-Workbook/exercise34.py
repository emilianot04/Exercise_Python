""" 
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60 percent. Write a program that begins by reading the number of loaves of day old bread being purchased from the user. Then your program should display the regular price for the bread, the discount because it is a day old, and the total price. Each of these amounts should be displayed on its own line with an appropriate label. All of the values should be displayed using two decimal places, and the decimal points in all of the numbers should be aligned when reasonable values are entered by the user.
"""

bread= 3.49
discount= 0.6

calculate = bread*discount

number_bread = int(input('Insert number loaves:'))


normal_price = bread * number_bread
discount_price = bread * number_bread* discount
total_discount = normal_price - discount_price


print('Sigle price: $' + '%.2f' % bread )
print('Single price discount: $' + '%.2f' % calculate )
print('Total price: $' + '%.2f' % normal_price )
print('Total price discount: $' + '%.2f' % discount_price )
print('Total  discount: $' + '%.2f' % total_discount )