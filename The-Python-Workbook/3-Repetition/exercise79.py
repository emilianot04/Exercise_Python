"""
The greatest common divisor of two positive integers, n and m, is the largest number, d, which divides evenly into both n and m. There are several algorithms that can be used to solve this problem, including:
Initialize d to the smaller of m and n.
While d does not evenly divide m or d does not evenly divide n do
Decrease the value of d by 1
Report d as the greatest common divisor of n and m
Write a program that reads two positive integers from the user and uses this algorithm to determine and report their greatest common divisor.
"""
import math

m = int(input("Insert first number integer: "))
n = int(input("Insert second number integer: "))
    
    
print ('The greatest common divisor of', m,  'and', n,  'is:', math.gcd(m, n))

