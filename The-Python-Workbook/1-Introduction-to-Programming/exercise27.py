""" 
Easter is celebrated on the Sunday immediately after the first full moon following the spring equinox. Because its date includes a lunar component, Easter does not have a fixed date in the Gregorian calendar. Instead, it can occur on any date between March 22 and April 25. The month and day for Easter can be computed for a given year using the Anonymous Gregorian Computus algorithm, which is shown below.
Set a equal to the remainder when year is divided by 19 
Set b equal to the floor of year divided by 100
Set c equal to the remainder when year is divided by 100 
Set d equal to the floor of b divided by 4
Set e equal to the remainder when b is divided by 4 Set f equaltothefloorof b+8/25
Setgequaltothefloorof b− f +1 3
Set h equal to the remainder when 19a + b − d − g + 15 is divided by 30 Set i equal to the floor of c divided by 4
Set k equal to the remainder when c is divided by 4
Set l equal to the remainder when 32 + 2e + 2i − h − k is divided by 7
Set m equal to the floor of a + 11h + 22l 451
   Setmonthequaltothefloorof h+l−7m+114 31
 Set day equal to one plus the remainder when h + l − 7m + 114 is divided by 31
Write a program that implements the Anonymous Gregorian Computus algorithm to compute the date of Easter. Your program should read the year from the user and then display a appropriate message that includes the date of Easter in that year.

"""

year = int(input('Insert year: '))

a = year % 19
b = year//100
c = year % 100
d = b//4
e = b % 4
f = (b+8)//25
g = (b-f+1)//3
h = ((19*a) + b - d - g + 15) % 30
i = c//4
k = c % 4
l = (32 + (2*e) + (2*i) - h - k) % 7
m = (a + (11*h) + (22 * l)) // 451
month = (h+l-(7*m)+114)//31
day = ((h+l - (7*m) + 114) % 31)+1

print(a, b, c, d, e, f, g, h, i, k, l, m, month, day)

if(month == 1):
    month_name = ('January')
elif(month == 2):
    month_name = ('February')
elif(month == 3):
    month_name = ('March')
elif(month == 4):
    month_name = ('April')
elif(month == 5):
    month_name = ('May')
elif(month == 6):
    month_name = ('June')
elif(month == 7):
    month_name = ('July')
elif(month == 8):
    month_name = ('August')
elif(month == 9):
    month_name = ('September')
elif(month == 10):
    month_name = ('October')
elif(month == 11):
    month_name = ('November')
elif(month == 12):
    month_name = ('December')

print('Easter is ' + str(day) + ' ' + month_name + ' ' + str(year))
