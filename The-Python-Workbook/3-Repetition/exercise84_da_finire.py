"""
What’s the minimum number of times you have to flip a coin before you can have three consecutive flips that result in the same outcome (either all three are heads or all three are tails)? What’s the maximum number of flips that might be needed? How many flips are needed on average? In this exercise we will explore these questions
by creating a program that simulates several series of coin flips.
Create a program that uses Python’s random number generator to simulate flipping a coin several times. The simulated coin should be fair, meaning that the probability of heads is equal to the probability of tails. Your program should flip simulated coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each time the outcome is heads, and a T each time the outcome is tails, with all of the outcomes for one simulation on the same line. Then display the number of flips that were needed to reach 3 consecutive occurrences of the same outcome. When your program is run it should perform the simulation 10 times and report the average
number of flips needed. Sample output is shown below:
"""

from random import randint

new_value = randint(1, 2)

head_count =0
tail_count=0
contatore= ''
n=0
for i in range(10):

    while head_count < 3 and tail_count <3:
        new_value = randint(1, 2)
        n=n+1
        if new_value == 1:
            print('H','\t', end = '') 
            head_count+= 1
        else:
            print('T','\t', end = '') 
            tail_count+= 1
     
    print(n,'flips','\n', end = '' )
    exit()
        
