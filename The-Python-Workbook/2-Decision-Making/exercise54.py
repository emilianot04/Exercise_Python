""" 
At a particular company, employees are rated at the end of each year. The rating scale begins at 0.0, with higher values indicating better performance and resulting in larger raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated with each rating is shown in the following table. The amount of an employee’s raise is $2,400.00 multiplied by their rating.

Write a program that reads a rating from the user and indicates whether the per- formance for that rating is unacceptable, acceptable or meritorious. The amount of the employee’s raise should also be reported. Your program should display an appropriate error message if an invalid rating is entered.

"""

rating = float(input('Insert a rating for the single user: '))

amount= 2400

if rating >= 0.0 and rating <= 0.3:
    meaning = 'Unacceptable Performance'
    value = 0
elif rating >= 0.4 and rating <= 0.5:
    meaning = 'Acceptable Performance'
    value = 0.4
elif rating >= 0.6:
    meaning = 'Meritorious Performance'
    value = 0.6
else: 
    letter = 'not valid'

calc = amount*value


print('The result is '+ meaning + ' the employee’s raise is ' '%.2f' % calc + '$')

