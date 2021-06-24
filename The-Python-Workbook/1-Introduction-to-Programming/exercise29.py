""" 
When the wind blows in cold weather, the air feels even colder than it actually is because the movement of the air increases the rate of cooling for warm objects, like people. This effect is known as wind chill.
In 2001, Canada, the United Kingdom and the United States adopted the following formula for computing the wind chill index. Within the formula Ta is the air temperature in degrees Celsius and V is the wind speed in kilometers per hour. 
A similar formula with different constant values can be used for temperatures in degrees Fahrenheit and wind speeds in miles per hour.
WCI = 13.12 + 0.6215Ta − 11.37V 0.16 + 0.3965Ta V 0.16
Write a program that begins by reading the air temperature and wind speed from the user. Once these values have been read your program should display the wind chill index rounded to the closest integer.
The wind chill index is only considered valid for temperatures less than or equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per hour.

"""

air_temperature = (float(input('Insert temperature(°C): ')))
if(air_temperature > 11):
    print('The temperatures less than or equal to 10 degrees Celsius')
    air_temperature = (float(input('Insert temperature(°C): ')))

velocity = (float(input('Insert Velocity (): ')))
if(air_temperature < 4.8):
    print('The wind speeds exceeding 4.8 kilometers per hour')
    velocity = (float(input('Insert Velocity (): ')))


WCI = 13.12 + 0.6215*air_temperature - 11.37 * \
    (velocity ** 0.16) + 0.3965 * air_temperature*(velocity ** 0.16)

print(' wind chill index is: ' '%.0f' % WCI + '°C')
