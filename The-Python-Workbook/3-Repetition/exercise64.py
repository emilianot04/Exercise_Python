""" 
A particular retailer is having a 60 percent off sale on a variety of discontinued products. The retailer would like to help its customers determine the reduced price of the merchandise by having a printed discount table on the shelf that shows the original prices and the prices after the discount has been applied. Write a program that uses a loop to generate this table, showing the original price, the discount amount, and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure that the discount amounts and the new prices are rounded to 2 decimal places when
they are displayed.
"""

discount_perc= 0.60
price= 4.95
offer= discount_perc* price
discount = price - offer
add = 5


print ('')
print ("Initial price\tDiscount(60%)\tFinal price")
print ('--------------------------------------------')

for i in range(5):
 
   print ("%.2f\t\t%.2f\t\t%.2f" % ( price,  discount, offer))
   price = price+add
   offer =  discount_perc * price  
   discount = price - offer
print ('--------------------------------------------')
print ('')




""" for i in range(5):
   print('')
   print('The initial price is: ' + str(price))
   print('The discount is: ' + '%.2f' % discount)
   print('The discount price is: ' + '%.2f' % offer)
   print('')
   price = price+add
   offer =  discount_perc * price  
   discount = price - offer


 """
    