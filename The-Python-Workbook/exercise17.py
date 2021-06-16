""" The amount of energy required to increase the temperature of one gram of a material by one degree Celsius is the material’s specific heat capacity, C. The total amount of energy, q, required to raise m grams of a material by ΔT degrees Celsius can be computed using the formula:
q = mCΔT
Write a program that reads the mass of some water and the temperature change from the user. Your program should display the total amount of energy that must be added or removed to achieve the desired temperature change.
Hint: The specific heat capacity of water is 4.186 J . Because water has a g◦C density of 1.0 grams per milliliter, you can use grams and milliliters inter- changeably in this exercise.
Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this exercise, you should assume that electricity costs 8.9 cents per kilowatt hour. Use your program to compute the cost of boiling the water needed for a cup of coffee.
Hint: You will need to look up the factor for converting between Joules and kilowatt hours to complete the last part of this exercise.
"""
import math
mass_water = float(input('Insert mass of water: '))
temperature_initial = float(input('Insert temperature initial: '))
temperature_final = float(input('Insert temperature initial: '))

q = mass_water* 4.184 * (temperature_final-temperature_initial)

kwh = q*2.77778

cost = kwh * 8.9 

print('Energy: ' + '%.2f' % q + ' joule' )
print('Costs: ' + '%.2f' %  cost + ' cents')

