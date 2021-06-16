""" 
It is commonly said that one human year is equivalent to 7 dog years. However this simple conversion fails to recognize that dogs reach adulthood in approximately two years. As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years, and then count each additional human year as 4 dog years.
Write a program that implements the conversion from human years to dog years described in the previous paragraph. Ensure that your program works correctly for conversions of less than two human years and for conversions of two or more human years. Your program should display an appropriate error message if the user enters a negative number.
"""
dog_year = int(input('Insert the years your dog:'))

if(dog_year >0):
    if(dog_year<=2):
        print (dog_year*10.5)
    elif(dog_year > 2):
        print ((dog_year*4)+21-2)
else:
    print('Error! the number is not positive')
    

