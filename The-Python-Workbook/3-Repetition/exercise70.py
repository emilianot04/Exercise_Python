""" 
A parity bit is a simple mechanism for detecting errors in data transmitted over an unreliable connection such as a telephone line. The basic idea is that an additional bit is transmitted after each group of 8 bits so that a single bit error in the transmission can be detected.
Parity bits can be computed for either even parity or odd parity. If even parity is selected then the parity bit that is transmitted is chosen so that the total number of one bits transmitted (8 bits of data plus the parity bit) is even. When odd parity is selected the parity bit is chosen so that the total number of one bits transmitted is odd.
Write a program that computes the parity bit for groups of 8 bits entered by the user using even parity. Your program should read strings containing 8 bits until the user enters a blank line. After each string is entered by the user your program should display a clear message indicating whether the parity bit should be 0 or 1. Display an appropriate error message if the user enters something other than 8 bits.
Hint: You should read the input from the user as a string. Then you can use the count method to help you determine the number of zeros and ones in the string. Information about the count method is available online.
"""

insert_bit = input('Insert 8 bit (blank to quit): ')

length = len(insert_bit)
zero = insert_bit.count('0')
one = insert_bit.count('1')

if (length != 8 or zero + one != 8):
    print('error')
else:
    bit = one

    if bit % 2 == 0:
        print('Parity bit = 0')
    else:
        print('Parity bit = 1')

insert_bit = input('Insert bit (blank to quit): ')
