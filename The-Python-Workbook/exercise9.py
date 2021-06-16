# Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, and is added to the balance of the savings account. Write a program that begins by reading the amount of money deposited into the account from the user. Then your program should compute and display the amount in the savings account after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places.

amount_initial = float(input('Insert you import: '))
interest = 4

amount = amount_initial * (interest/100)

year1 = amount_initial + amount
year2 = amount_initial + amount*2
year3 = amount_initial + amount*3
print('Amount after 1 year: ' + '%.2f' % year1)
print('Amount after 2 year: ' + '%.2f' % year2)
print('Amount after 3 year: ' + '%.2f' % year3)


