# Create a program that reads the length and width of a farmer’s field from the user in feet. Display the area of the field in acres.

width= input('Insert width:\n')
length = input('Insert lenght:\n')

feet = (float(width)*float(length))
acre = feet * 43.560

print('The area of the room is: ' + str(acre) + ' feet')
