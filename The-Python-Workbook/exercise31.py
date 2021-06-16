""" 
In this exercise you will create a program that reads a pressure from the user in kilo- pascals. Once the pressure has been read your program should report the equivalent pressure in pounds per square inch, millimeters of mercury and atmospheres. Use your research skills to determine the conversion factors between these units.
"""

Pressure = (float(input('Insert pressure(°K/P): ')))
PSI = Pressure*0.145
MOM = Pressure * 7.5006
ATM = Pressure * 0.0099

print('°K/P: ' '%.0f' % Pressure + '; PSI: ' '%.4f' %
      PSI + '; MOM: ' '%.4f' % MOM + '; ATM: ' '%.4f' % ATM)
