""" 
In this exercise you will create a program that computes the average of a collection of values entered by the user. The user will enter 0 as a sentinel value to indicate that no further values will be provided. Your program should display an appropriate error message if the first value entered by the user is 0.
Hint: Because the 0 marks the end of the input it should not be included in the average.

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

    print('The sum of the '+str(n) + 'entered is: ' +
          str(sum) + ' and the average is:' + '%.2f' % average)
