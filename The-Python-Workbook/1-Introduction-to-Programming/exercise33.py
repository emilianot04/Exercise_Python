""" 
Create a program that reads three integers from the user and displays them in sorted order (from smallest to largest). Use the min and max functions to find the smallest and largest values. The middle value can be found by computing the sum of all three values, and then subtracting the minimum value and the maximum value.
"""

Number1 = int(input('Insert first number integer:'))
Number2 = int(input('Insert second number integer:'))
Number3 = int(input('Insert third number integer:'))



value_max = max(Number1,Number2,Number3)
value_min = min(Number1,Number2,Number3)
sum= Number1+Number2+Number3
value_medium = sum - value_max- value_min

print(value_min,value_medium,value_max)
