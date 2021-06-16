""" 
Write a program that determines the name of a shape from its number of sides. Read the number of sides from the user and then report the appropriate name as part of a meaningful message. Your program should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of sides outside of this range is entered then your program should display an appropriate error message.
"""
shape = int(input('Insert the number of sides:'))


if(shape>3 and shape  < 10 ):
    if(shape==3):
        print ('is a triangle')
    if(shape==4):
        print ('is a square')
    if(shape==5):
        print ('is a pentagon')
    if(shape==6):
        print ('is a esagon')
    if(shape==7):
        print ('is a heptagon')
    if(shape==8):
        print ('is a octagon')
    if(shape==9):
        print ('is a ennagon')
    if(shape==10):
        print ('is a decagon')
else:
    print('the number must be between 3 and 10')


