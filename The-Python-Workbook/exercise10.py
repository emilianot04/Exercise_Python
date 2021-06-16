import math
""" Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a 
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of ab """

a = float(input('Insert a: '))
b = float(input('Insert b: '))

sum = a+b
difference = b - a
product = a*b
quotient = a/b
remainder = a % b
log = math.log10(a)
result = a**b

print(sum, difference, product, quotient, remainder, log, result)
