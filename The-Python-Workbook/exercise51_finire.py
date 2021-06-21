""" 
A univariate quadratic function has the form f (x) = ax2 + bx + c, where a, b and c are constants, and a is non-zero. Its roots can be identified by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0. These values can be computed using the quadratic formula, shown below. A quadratic function may have 0, 1 or 2 real roots.
The portion of the expression under the square root sign is called the discriminant. If the discriminant is negative then the quadratic equation does not have any real roots. If the discriminant is 0, then the equation has one real root. Otherwise the equation has two real roots, and the expression must be evaluated twice, once using a plus sign, and once using a minus sign, when computing the numerator.
Write a program that computes the real roots of a quadratic function. Your pro- gram should begin by prompting the user for the values of a, b and c. Then it should display a message indicating the number of real roots, along with the values of the real roots (if any).

"""

a = float(input('Insert a: '))
b = float(input('Insert b: '))
c = float(input('Insert c: '))


if magnitude >= 0 and magnitude <= 10:
    if magnitude < 2:
        description = "Micro"
    elif magnitude >= 2 and magnitude < 3:
        description = "Very Minor"
    elif magnitude >= 3 and magnitude < 4:
        description = "Minor"
    elif magnitude >= 4 and magnitude < 5:
        description = "Light"
    elif magnitude >= 5 and magnitude < 6:
        description = "Moderate"
    elif magnitude >= 6 and magnitude < 7:
        description = "Strong"
    elif magnitude >= 7 and magnitude < 8:
        description = "Major"
    elif magnitude >= 8 and magnitude < 10:
        description = "Great"
    elif magnitude >= 10:
        description = "Meteoric"
    print('The Magnitude ' + str(magnitude) + ' is ' + description)
else:
    print('The value is not valid (between 0 and 10.00)')
