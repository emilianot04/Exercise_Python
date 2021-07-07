""" 
Exercise 52 includes a table that shows the conversion from letter grades to grade points at a particular academic institution. In this exercise you will compute the grade point average of an arbitrary number of letter grades entered by the user. The user will enter a blank line to indicate that all of the grades have been provided. For example, if the user enters A, followed by C+, followed by B, followed by a blank line then your program should report a grade point average of 3.1.
You may find your solution to Exercise 52 helpful when completing this exercise. Your program does not need to do any error checking. It can assume that each value entered by the user will always be a valid letter grade or a blank line.
"""

vote  =input('Insert vote (blank to quit): ')
vote = vote.upper()

sum = 0
n = 0
while vote != "":
    n = n+1

    if vote == 'A+' or vote == 'A' :
        grade = 4.0
    elif vote == 'A-':
        grade = 3.7
    elif vote == 'B+':
        grade = 3.3
    elif vote == 'B':
        grade = 3.0
    elif vote == 'B-':
        grade = 2.7
    elif vote == 'C+':
        grade = 2.3
    elif vote == 'C':
        grade = 2.0
    elif vote == 'C-':
        grade = 1.7
    elif vote == 'D+':
        grade = 1.3
    elif vote == 'D':    
        grade = 1.0
    elif vote == 'F':    
        grade = 0
    else:
        print('Vote not valid')
        n = n-1
        grade = 0 
        
   
    sum = sum + grade
    average = sum/n
    vote  =input('Insert vote  (blank to quit): ')
    vote = vote.upper()


print("The average vote is ", str(average))
