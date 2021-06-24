""" 
At a particular university, letter grades are mapped to grade points in the following manner:
Write a program that begins by reading a letter grade from the user. Then your program should compute and display the equivalent number of grade points. Ensure that your program generates an appropriate error message if the user enters an invalid letter grade.

"""

grade = float(input('Insert a letter grade: '))

if grade == 4 :
    letter = 'A+ or A'
elif grade <= 3.9 and grade >= 3.7:
    letter = 'A-'
elif grade <= 3.6 and grade >= 3.3:
    letter =  'B+'
elif grade <= 3.2 and grade >= 3.0:
    letter = 'B'
elif grade <= 2.9 and grade >= 3.7:
    letter =  'B-'
elif grade <= 2.6 and grade >= 2.3:
    letter =  'C+'
elif grade <= 2.2 and grade >= 2:
    letter =  'C'
elif grade <= 1.9 and grade >= 1.7:
    letter = 'C-'
elif grade <= 1.6 and grade >= 1.3:
    letter = 'D+'
elif grade <= 1.2 and grade >= 1:  
    letter = 'D'
elif grade <= 0.9 and grade >=0:  
    letter = 'F'
else: 
    letter = 'not valid'


print('The equivalent from  grade point ' + str(grade) + ' Magnitude letter is ' + letter)

