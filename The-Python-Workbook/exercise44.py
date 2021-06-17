""" 
It is common for images of a country’s previous leaders, or other individuals of his- torical significance, to appear on its money. The individuals that appear on banknotes
in the United States are listed in below.
Write a program that begins by reading the denomination of a banknote from the user. Then your program should display the name of the individual that appears on the banknote of the entered amount. An appropriate error message should be displayed if no such note exists.
"""

banknote = float(input('Insert denomination of a banknote ($): '))
name = 'not exist'

if banknote == 1:
    name = 'George Washington'
elif banknote == 2:
    name = 'Thomas Jefferson'
elif banknote == 5:
    name = 'Abraham Lincoln'
elif banknote == 10:
    name = 'Alexander Hamilton'
elif banknote == 20:
    name = 'Andrew Jackson'
elif banknote == 50:
    name = 'Ulysses S. Grant'
elif banknote == 100:
    name = 'Benjamin Franklin'

print('The banknote is ' + name)


""" else:
    name=''

if name=='':
    print('The banknote not exist')
else:
    print('The banknote is ' + name)
 """