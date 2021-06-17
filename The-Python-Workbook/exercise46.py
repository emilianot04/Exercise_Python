""" 
Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row, as shown below:
Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black square or a white square. Then use modular arithmetic to report the color of the square in that row. For example, if the user enters a1 then your program should report that the square is black. If the user enters d5 then your program should report that the square is white. Your program may assume that a valid position will always be entered. It does not need to perform any error checking.

"""

letter = input('Insert letter: ')
numbers = int(input('Insert number: '))

if (letter >= 'a' and letter <= 'h') and (numbers >= 1 and numbers <= 8):
    if(letter == 'a' or letter == 'c' or letter == 'e' or letter == 'g') and (numbers % 2):
        color = 'the square is black'
    else:
        color = 'the square is black'
    print(color)
else:
    print('Insert a valid date (from a to h and from 1 to 8')
