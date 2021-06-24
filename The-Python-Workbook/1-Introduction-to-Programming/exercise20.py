""" The ideal gas law is a mathematical approximation of the behavior of gasses as
pressure, volume and temperature change. It is usually stated as:
PV = nRT
where P is the pressure in Pascals, V is the volume in liters, n is the amount of
substance in moles, R is the ideal gas constant, equal to 8.314 J , and T is the
temperature in degrees Kelvin.
Write a program that computes the amount of gas in moles when the user supplies the pressure, volume and temperature. Test your program by determining the number of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is approximately 20 degrees Celsius or 68 degrees Fahrenheit.
Hint: A temperature is converted from Celsius to Kelvin by adding 273.15 to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it, multiply it by 59 and then add 273.15 to it.
"""

import math
pressure = float(input('Insert pressure (Pascal): '))
volume = float(input('Insert volume (liters): '))
temperature = float(input('Insert temperature (°K): '))
R = 8.31446261815324

temperature_celsius = temperature + 273.15

print(temperature_celsius)

n = (pressure * volume) / (R*temperature_celsius)


print('moles of gas: ' +  '%.2f' % n )
