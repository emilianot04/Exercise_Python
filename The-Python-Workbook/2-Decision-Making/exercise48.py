""" 
The horoscopes commonly reported in newspapers use the position of the sun at the time of one’s birth to try and predict the future. This system of astrology divides the
year into twelve zodiac signs, as outline in the table below:

Write a program that asks the user to enter his or her month and day of birth. Then your program should report the user’s zodiac sign as part of an appropriate output message.

"""

day = int(input('Insert day: '))
month = input('Insert month: ')
sign = ''
if(day >= 1 and day <= 31) and (month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June' or month == 'July' or month == 'August' or month == 'September' or month == 'October' or month == 'November' or month == 'December'):
    if(month == 'January'):
        if(day == day >= 1 and day <= 19):
            sign = 'Capricorn'
        else:
            sign = 'Aquarius'
    elif(month == 'February'):
        if day == day >= 1 and day <= 18:
            sign = 'Aquarius'
        else:
            sign = 'Pisces'
    elif(month == 'March'):
        if(day == day >= 1 and day <= 20):
            sign = 'Pisces'
        else:
            sign = 'Aries'
    elif(month == 'April'):
        if(day == day >= 1 and day <= 19):
            sign = 'Aries'
        else:
            sign = 'Taurus'
    elif(month == 'May'):
        if(day == day >= 1 and day <= 20):
            sign = 'Taurus'
        else:
            sign = 'Gemini'
    elif(month == 'June'):
        if(day == day >= 1 and day <= 20):
            sign = 'Gemini'
        else:
            sign = 'Cancer'
    elif(month == 'July'):
        if(day == day >= 1 and day <= 22):
            sign = 'Cancer'
        else:
            sign = 'Leo'
    elif(month == 'August'):
        if(day == day >= 1 and day <= 22):
            sign = 'Leo'
        else:
            sign = 'Virgo'
    elif(month == 'September'):
        if(day == day >= 1 and day <= 22):
            sign = 'Virgo'
        else:
            sign = 'Libra'
    elif(month == 'October'):
        if(day == day >= 1 and day <= 22):
            sign = 'Libra'
        else:
            sign = 'Scorpio'
    elif(month == 'November'):
        if(day == day >= 1 and day <= 21):
            sign = 'Scorpio'
        else:
            sign = 'Sagittarius'
    elif(month == 'December'):
        if(day == day >= 1 and day <= 21):
            sign = 'Sagittarius'
        else:
            sign = 'Capricorn'

    print('Anyone born on ' + str(day) + ' ' + month + ' is of the zodiac sign of ' + sign)
else:
    print('Value not valid')
