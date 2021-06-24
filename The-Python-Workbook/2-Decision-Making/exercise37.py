""" 
In this exercise you will create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel. If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.
"""
letter = str(input('Insert a letter of alphabet:'))


if(letter == 'a' or letter =='e' or letter =='i' or letter =='o' or letter =='u' ):
    print (letter + ' is a vowel')
elif(letter == 'y'):
    print (letter + ' Sometimes is a vowel, and sometimes is a consonant.')
else:
    print( letter + ' is a consonant')


