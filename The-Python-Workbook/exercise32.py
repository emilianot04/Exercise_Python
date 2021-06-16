""" 
Develop a program that reads a four-digit integer from the user and displays the sum of its digits. For example, if the user enters 3141 then your program should display
3+1+4+1=9.
"""

Number = int(input('Insert number four-digit integer:'))
Number_string = str(Number)
sum = 0

for i in str(Number):
    sum = sum+int(i)

print(Number_string[0] + '+' + Number_string[1] + '+' +
      Number_string[2] + '+' + Number_string[3] + '=' + str(sum))
