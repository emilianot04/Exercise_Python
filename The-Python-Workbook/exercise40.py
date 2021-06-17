""" 
The following table lists the sound level in decibels for several common noises.
 Noise
Jackhammer Gas Lawnmower Alarm Clock Quiet Room
Decibel Level
130 dB 106 dB 70 dB 40 dB
  Write a program that reads a sound level in decibels from the user. If the user enters a decibel level that matches one of the noises in the table then your program should display a message containing only that noise. If the user enters a number of decibels between the noises listed then your program should display a message indicating which noises the value is between. Ensure that your program also generates reasonable output for a value smaller than the quietest noise in the table, and for a value larger than the loudest noise in the table.
"""

user_decibel = int(input('Insert decibel: '))
if(user_decibel < 40 ):
    print('The value smaller than the quietest noise')
elif(user_decibel > 130):
    print('The value larger than the quietest noise') 
else:
    if(user_decibel == 130):
        decibel = 'Jackhammer'
    elif(user_decibel > 106 and  user_decibel < 130):
        decibel = ' beetween Jackhammer and Gas Lawnmower'
    elif(user_decibel == 106 ):
        decibel = 'Gas Lawnmower'
    elif(user_decibel > 70 and user_decibel < 106):
        decibel = 'beetween Gas Lawnmower and Alarm Clock'
    elif(user_decibel == 70 ):
        decibel = 'Alarm Clock'
    elif(user_decibel >  40 and user_decibel < 70):
        decibel = 'beetween Alarm Clock and Quiet Room'
    elif(user_decibel == 40 ):
        decibel = 'Quiet Room'
    print('The noise is ' + str(decibel))

