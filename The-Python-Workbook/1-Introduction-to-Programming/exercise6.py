# The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local tax rate when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. Format the output so that all of the values are displayed using two decimal places.

meal = float(input('Insert price: '))
tax = 20
meal_tax = meal * 20/100
tip = 18
meal_tip = meal * 18/100


totale = meal + meal_tip + meal_tax
print('prezzo: ' + '%.2f' % float(meal))
print('tasse: ' + '%.2f' % meal_tax)
print('mancia: ' + '%.2f' % meal_tip)
print('totale :' + '%.2f' % totale)
