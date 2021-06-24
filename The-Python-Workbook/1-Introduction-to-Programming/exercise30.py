""" 
Write a program that begins by reading a temperature from the user in degrees Celsius. Then your program should display the equivalent temperature in degrees Fahrenheit and degrees Kelvin. The calculations needed to convert between different units of temperature can be found on the Internet.

"""

Celsius = (float(input('Insert temperature(°C): ')))
Kelvin = Celsius + 273.15
Fahrenheit = Celsius*(9/5) + 32

print('Celsius: ' '%.2f' % Celsius + '°C' ', Fahrenheit: '  '%.2f' %
      Fahrenheit + '°F'', Kelvin: '  '%.2f' % Kelvin + '°K'),
