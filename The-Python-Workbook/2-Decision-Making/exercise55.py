""" 
Electromagnetic radiation can be classified into one of 7 categories according to its frequency, as shown in the table below:

Write a program that reads the frequency of some radiation from the user and displays name of the radiation as part of an appropriate message.
"""

wavelength = int(input('Insert a wavelength(nm): '))

if wavelength >= 380 and wavelength <=750:
    if wavelength >= 380 and wavelength < 450:
        color = 'Violet'
    if wavelength >= 450 and wavelength < 495:
        color = 'Blue'
    elif wavelength >= 495 and wavelength < 570:
        color = 'Green'
    elif wavelength >= 570 and wavelength < 590:
        color = 'Yellow'   
    elif wavelength >= 590 and wavelength < 620:
        color = 'Orange'
    elif wavelength >= 620 and wavelength < 750:
        color = 'Red'
    print('The color with ' + str(wavelength) + ' wavelength is ' + color)
else: 
    print('The wavelength must be between 380 and 750')