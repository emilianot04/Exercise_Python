""" 
The following table contains earthquake magnitude ranges on the Richter scale and their descriptors:
Write a program that reads a magnitude from the user and displays the appropriate descriptor as part of a meaningful message. For example, if the user enters 5.5 then your program should indicate that a magnitude 5.5 earthquake is considered to be a moderate earthquake.

"""

magnitude = float(input('Insert magnitude: '))
if magnitude >= 0 and magnitude<=10:
    if magnitude <2:
        description = "Micro"
    elif magnitude >=2 and magnitude <3: 
        description = "Very Minor"
    elif magnitude >=3 and magnitude <4: 
        description = "Minor"
    elif magnitude >=4 and magnitude <5: 
        description = "Light"
    elif magnitude >=5 and magnitude <6: 
        description = "Moderate"
    elif magnitude >=6 and magnitude <7: 
        description = "Strong"
    elif magnitude >=7 and magnitude <8: 
        description = "Major"
    elif magnitude >=8 and magnitude <10: 
        description = "Great"
    elif magnitude >=10: 
        description = "Meteoric"
    print('The Magnitude ' + str(magnitude)  + ' is ' + description)
else:
    print('The value is not valid (between 0 and 10.00)')