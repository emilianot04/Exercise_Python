""" Create a program that determines how quickly an object is travelling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration 
due to gravity is 9.8 m/s . You can use the formula vf = vi + 2ad to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.
"""

import math
a = float(input('Insert accelerate (m/s): '))
d = float(input('Insert distance (m): '))
initial_velocity = 0


final_speed = math.sqrt(initial_velocity + 2*(a*d))

print('Final speed is: ' + '%.2f' % final_speed + ' m/s')
