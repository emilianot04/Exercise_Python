""" 
February 4, 2013 was the last day that pennies were distributed by the Royal Canadian Mint. Now that pennies have been phased out retailers must adjust totals so that they are multiples of 5 cents when they are paid for with cash (credit card and debit card transactions continue to be charged to the penny). While retailers have some freedom in how they do this, most choose to round to the closest nickel.
Write a program that reads prices from the user until a blank line is entered.
Display the total cost of all the entered items on one line, followed by the amount due if the customer pays with cash on a second line. The amount due for a cash payment should be rounded to the nearest nickel. One way to compute the cash payment amount is to begin by determining how many pennies would be needed to pay the total. Then compute the remainder when this number of pennies is divided by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust the total up.

"""

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
            
            
     
      print('The price of the' + str(n) + 'article is: ' + str(sum))
      print('The price with card is: ' + str(sum))
      
sum2 = sum *100

if(sum2 %5 == 0):
      print(sum)
else:
      print(sum+ 0.5)

  



    
