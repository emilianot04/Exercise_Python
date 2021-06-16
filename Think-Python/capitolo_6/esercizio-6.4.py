#MCD massimo comun divisore (MCD) 
import math
def mcd (a,b):
     return math.gcd(a, b)

print(mcd(70,15))

#mcd 
def euclide(a, b):
    while(b != 0):
        r=a%b
        a=b
        b=r
    return a
 
print(euclide(70,15)) # 5