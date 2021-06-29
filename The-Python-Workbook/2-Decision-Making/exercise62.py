""" 
A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers between 1 and 36 are used to number the black spaces.
Many different bets can be placed in roulette. We will only consider the following
subset of them in this exercise:
• Single number (1 to 36, 0, or 00)
• Red versus Black
• Odd versus Even (Note that 0 and 00 do not pay out for even) • 1to18versus19to36
Write a program that simulates a spin of a roulette wheel by using Python’s random number generator. Display the number that was selected and all of the bets that must be payed. For example, if 13 is selected then your program should display:
The spin resulted in 13... Pay 13
Pay Black
Pay Odd
Pay 1 to 18
If the simulation results in 0 or 00 then your program should display Pay 0 or Pay 00 without any further output.

"""

import random
number_random = random.randint(0, 37)

# if random number is 37 change in 00
if(number_random == 37):
    number_random = '00'

print('The spin resulted in: ' + str(number_random))

# red, black or green

if ((number_random == 1) or (number_random == 3) or (number_random == 5) or (number_random == 7) or (number_random == 9) or (number_random == 12) or (number_random == 14) or (number_random == 16) or (number_random == 18) or (number_random == 19) or (number_random == 21) or (number_random == 23) or (number_random == 25) or (number_random == 27) or (number_random == 30) or (number_random == 32) or (number_random == 34) or (number_random == 36)):
    print('Pay ' + str(number_random))
    print('Pay Red')
elif ((number_random == 0) or (number_random == '00')):
    print('Pay ' + str(number_random))
else:
    print('Pay ' + str(number_random))
    print('Pay Black')


# trasform 00 in 37
if(number_random == '00'):
    number_random = 37

# if number is beetween from 1 to 36 print even or odd
if (1 < number_random <= 36):
    if(number_random % 2 == 0):
        print('Pay Even')
    elif(number_random % 2 == 1):
        print('Pay Odd')

# the numbers will be divided into two groups
if(1 < number_random <= 18):
    print('Pay 1 to 18')
elif(19 < number_random <= 36):
    print('Pay 19 to 36')
