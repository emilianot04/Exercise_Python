""" 
In a particular jurisdiction, older license plates consist of three uppercase letters followed by three digits. When all of the license plates following that pattern had been used, the format was changed to four digits followed by three uppercase letters. Write a program that begins by reading a string of characters from the user. Then your program should display a message indicating whether the characters are valid for an older style license plate or a newer style license plate. Your program should display an appropriate message if the string entered by the user is not valid for either style of license plate.
"""
# user's inputs
plate = input('Insert plate: ')

if(len(plate)==6):
    if (plate[0:2].isalpha) and (int(plate[3:5])<999):
       print('targa vecchia')
    else:
        print('non valida')
elif(len(plate)==7):
    if (plate[0:3].isalpha) and (int(plate[4:6])<999):
       print('targa nuova')
    else:
        print('non valida')
else:
        print('non valida')
