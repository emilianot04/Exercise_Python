""" 
The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the spectrum is continuous, it is often divided into 6 colors as shown below:

Write a program that reads a wavelength from the user and reports its color. Display an appropriate error message if the wavelength entered by the user is outside of the visible spectrum.

"""

frequency = float(input('Insert a frequency(Ghz): '))

HZ = 1e9
frequency_convertion  = HZ * frequency   # e == **

if ( 3e9 <= frequency_convertion  <= 3e19):
    if frequency_convertion <3e9:
        color = 'Radio Waves'
    elif frequency_convertion >= 3e9 and frequency_convertion < 3e12:
        color = 'Microwaves'
    elif frequency_convertion >= 3e12 and frequency_convertion < 4.3e14:
        color = 'Infrared Light '
    elif frequency_convertion >= 4.3e14 and frequency_convertion < 7.5e14:
        color = 'Visible Light'   
    elif frequency_convertion >= 7.5e14 and frequency_convertion < 3e17:
        color = 'Ultraviolet Ligh'
    elif frequency_convertion >= 3e17 and frequency_convertion < 3e19:
        color = 'X-Rays'
    elif frequency_convertion > 3e19:
        color = 'Gamma Rays'
    print('The name with', color , 'frequency_convertion', frequency_convertion)
else: 
    print('The frequency must be between 3e) and 3e19)')


