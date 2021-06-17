""" 
In the previous question you converted from a note’s name to its frequency. In this question you will write a program that reverses that process. Begin by reading a frequency from the user. If the frequency is within one Hertz of a value listed in the table in the previous question then report the name of the corresponding note. Otherwise report that the frequency does not correspond to a known note. In this exercise you only need to consider the notes listed in the table. There is no need to
consider notes from other octaves.
"""

frequency = float(input('Insert the frequency in Hz: '))
note = 'no valid'
if frequency == 261.63:
    note = 'C'
elif frequency == 293.66:
    note = 'D'
elif frequency == 329.63:
    note = 'E'
elif frequency == 349.23:
    note = 'F'
elif frequency == 392.00:
    note = 'G'
elif frequency == 440.00:
    note = 'A'
elif frequency == 493.88:
    note = 'B'

print('The name note is ' + note)
