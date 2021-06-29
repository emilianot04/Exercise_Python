""" 
In a particular jurisdiction, older license plates consist of three uppercase letters followed by three digits. When all of the license plates following that pattern had been used, the format was changed to four digits followed by three uppercase letters. Write a program that begins by reading a string of characters from the user. Then your program should display a message indicating whether the characters are valid for an older style license plate or a newer style license plate. Your program should display an appropriate message if the string entered by the user is not valid for either style of license plate.
"""
# user's inputs
plate = input('Insert plate,example [ABC123] OR [1234ABC]: ')

if(plate.isupper()):
   # ABC123
    if(len(plate) == 6):
        if ((plate[0:2]) > 'A' and (plate[0:2]) < 'Z') and (int(plate[3:5]) > 000 and (int(plate[3:5])) < 999):
            print('The plate ' + plate + ' is old')
        else:
            print('The plate ' + plate + ' is not valid')
    # 1234ABC
    elif(len(plate) == 7):
        if (int(plate[0:3]) > 0000 and (int(plate[0:3])) < 9999) and ((plate[4:7]) > 'A' and (plate[4:7]) < 'Z'):
            print('The plate ' + plate + ' is new')
        else:
            print('The plate ' + plate + ' is not valid')
    else:
        print('The plate ' + plate + ' is not valid')
else:
    print('The plate ' + plate + ' is not valid')
