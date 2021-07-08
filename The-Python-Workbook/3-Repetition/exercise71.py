""" 
nilakantha series
The value of π can be approximated by the following infinite series:
44444 π≈3+−+−+−···
     2 × 3 × 4 4 × 5 × 6 6 × 7 × 8 8 × 9 × 10 10 × 11 × 12
Write a program that displays 15 approximations of π. The first approxima- tion should make use of only the first term from the infinite series. Each additional approximation displayed by your program should include one more term in the series, making it a better approximation of π than any of the approximations displayed pre- viously.
"""


iter = 0
pi = 3

for a in range(2, 32, 2):
    b = a+1
    c = a+2

    if(iter % 2):
        pi = pi - 4/(a*b*c)
    else:
        pi = pi + 4/(a*b*c)
    iter += 1

    print(str(iter) + " π = " + str(pi))
