""" 
The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the spectrum is continuous, it is often divided into 6 colors as shown below:

Write a program that reads a wavelength from the user and reports its color. Display an appropriate error message if the wavelength entered by the user is outside of the visible spectrum.

"""

number = float(input('Insert a frequency: '))

elevate = int(input('Insert a elevete: '))

fq = number*(10**elevate)


if (number >= 3 and number <= 7.5)  and (elevate >= 9 and elevate <= 19): 
    if fq >= 3*(10**9):
        color = 'Radio Waves'
    elif fq >= 3*(10**9) and fq < 3*(10**12):
        color = 'Microwaves'
    elif fq >= 3*(10**12) and fq < 4.3*(10**14):
        color = 'Infrared Light '
    elif fq >= 4.3*(10**14) and fq < 7.5*(10**14):
        color = 'Visible Light'   
    elif fq >= 7.5*(10**14) and fq < 3*(10**17):
        color = 'Ultraviolet Ligh'
    elif fq >= 3*(10**17) and fq < 3*(10**19):
        color = 'X-Rays'
    elif fq > 3*(10**9):
        color = 'Gamma Rays'
    print('The name with ' + str(number) + ' elevate ' + str(elevate)+ ' is: ' + color)
else: 
    print('The frequency must be between 3*(10**9) and 3*(10**19)')


