""" Words like first, second and third are referred to as ordinal numbers. In this exercise, you will write a function that takes an integer as its only parameter and returns a string containing the appropriate English ordinal number as its only result. Your function must handle the integers between 1 and 12 (inclusive). It should return an empty string if the function is called with an argument outside of this range. Include a main program that demonstrates your function by displaying each integer from 1 to 12 and its ordinal number. Your main program should only run when your file has not been imported into another program.

 """


def ordinal(number):

    if number ==1:
        ordinal = 'first'
    elif number ==2:
        ordinal = 'Second'
    elif number ==3:
        ordinal = 'Third'
    elif number ==4:
        ordinal = 'Fourth'
    elif number ==5:
        ordinal = 'Fifth'
    elif number ==6:
        ordinal = 'Sixth'
    elif number ==7:
        ordinal = 'Seventh'
    elif number ==8:
        ordinal = 'Eighth'
    elif number ==9:
        ordinal = 'Ninth'
    elif number ==10:
        ordinal = 'Tenth'
    elif number ==11:
        ordinal = 'Eleventh'
    elif number ==12:
        ordinal = 'Twelfth'
    else:
        print('The number entered is incorrect')
        quit()

    return ordinal

def main():

    number= int(input("Insert number between 1 an 12 : "))
    print('the number corresponding to', number, 'in ordinal mode is', ordinal(number))


if __name__ == "__main__":
    main()
