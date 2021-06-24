""" In the United States, fuel efficiency for vehicles is normally expressed in miles-per- gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100km). Use your research skills to determine how to convert from MPG to L/100 km. Then create a program that reads a value from the user in American units and displays the equivalent fuel efficiency in Canadian units.
 """
american_units = float(input('Insert american_units: '))

canadian_units = float(american_units) * 0.425144

print('American units: ' + '%.2f' % american_units + ' MPG')
print('equal in Canadian units: ' + '%.2f' % float(canadian_units) + ' LTH')
