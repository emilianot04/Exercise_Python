""" 
At a particular university, letter grades are mapped to grade points in the following manner:
Write a program that begins by reading a letter grade from the user. Then your program should compute and display the equivalent number of grade points. Ensure that your program generates an appropriate error message if the user enters an invalid letter grade.

"""

letter = input('Insert a letter grade: ')

if letter == 'A+' or letter == 'A' :
    grade = 4.0
elif letter == 'A-':
    grade = 3.7
elif letter == 'B+':
    grade = 3.3
elif letter == 'B':
    grade = 3.0
elif letter == 'B-':
    grade = 2.7
elif letter == 'C+':
    grade = 2.3
elif letter == 'C':
    grade = 2.0
elif letter == 'C-':
    grade = 1.7
elif letter == 'D+':
    grade = 1.3
elif letter == 'D':    
    grade = 1.0
elif letter == 'F':    
    grade = 0
else: 
    grade = 'not valid'


print('The equivalent from Magnitude letter ' + letter + ' is grade point ' + str(grade))

