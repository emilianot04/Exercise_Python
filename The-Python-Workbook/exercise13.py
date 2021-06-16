""" Consider the software that runs on a self-checkout machine. One task that it must be able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the coins that should be used to give that amount of change to the shopper. The change should be given using as few coins as possible. Assume that the machine is loaded with pennies, nickels, dimes, quarters, loonies and toonies.
A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie because one side of the coin has a loon (a type of bird) on it. The two dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is derived from the combination of the number two and the name of the loonie. """

coins = int(input('Insert money in cents:'))
cent1 = 1
cent2 = 2
cent5 = 5
cent10 = 10
cent20 = 20
cent50 = 50


total_cents50 = coins//cent50
total_rest50 = coins%cent50
total_cents20 = total_rest50//cent20
total_rest20 = total_rest50%cent20
total_cents10 = total_rest20//cent10
total_rest10 = total_rest20%cent10
total_cents5 = total_rest10//cent5
total_rest5 = total_rest10%cent5
total_cents2 = total_rest5//cent2
total_rest2 = total_rest5%cent2
total_cents1 = total_rest5//cent1

print('Coins from 50 cents: ' + str(total_cents50))
print('Coins from 20 cents: ' + str(total_cents20))
print('Coins from 10 cents: ' + str(total_cents10))
print('Coins from 5 cents: ' + str(total_cents5))
print('Coins from 2 cents: ' + str(total_cents2))
print('Coins from 1 cents: ' + str(total_cents1))