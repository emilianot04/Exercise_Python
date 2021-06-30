""" 
Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit. The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate headings on your columns. The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the Internet.
"""


tc = 1
tf = (1.8*tc) + 32 
print ('')
print ("Temperature\tCelsius\t\tFahrenheit")
print ('--------------------------------------------')

for i in range (0,101,10):
 
   tc = int(i)
   tf = (int(1.8*i) + 32)  
   print ("%s°\t\t%s°C\t\t%s°F" % (i, tc, tf))

print ('--------------------------------------------')
print ('')



  



    
