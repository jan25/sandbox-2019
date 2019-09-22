from shapes.triangle import Triangle
'''
This import wouldn't work:
from .triangle import Triangle

Run this file using:
$ python3 -m shapes
'''

a, b, c = 3, 2, 3
print('Test triangle')
print('Sides: %d %d %d' % (a, b, c))
print('Perimeter: %d' % Triangle(a, b, c).perimeter())
print('Area: %f' % Triangle(a, b, c).area())
