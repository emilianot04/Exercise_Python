""" 
A particular retailer is having a 60 percent off sale on a variety of discontinued products. The retailer would like to help its customers determine the reduced price of the merchandise by having a printed discount table on the shelf that shows the original prices and the prices after the discount has been applied. Write a program that uses a loop to generate this table, showing the original price, the discount amount, and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure that the discount amounts and the new prices are rounded to 2 decimal places when
they are displayed.
"""

number = int(input('Insert number[0 to esc]: '))

sum = 0
n = 0
average = 0

if(number == 0):
    print('Value 0 is not valid')
else:
    while number != 0:
        sum = number+sum
        n = n+1
        average = sum/n
        number = int(input('Insert number[0 to esc]: '))

    print('The sum of the '+str(n) + ' entered is: ' +
          str(sum) + ' and the average is: ' + '%.2f' % average)


    
