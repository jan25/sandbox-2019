'''
.. module:: triangle

Triangle shape. I'm with 3 sides, remember?
'''
import shapes.mymath as mymath

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return mymath.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_equivalent(self):
        '''
        Use this to check if Triangle is a equivalent triangle.
        i.e. if all sides are the same

        :returns: bool -- if equivalent
        '''
        return self.a == self.b and self.b == self.c
    
    def is_right_triangle(self):
        '''
        Use this to check if triangle if a right triangle
        i.e. if c^2 = a^2 + b^2

        :returns: bool -- if right
        '''
        a, b, c = sorted([self.a, self.b, self.c])
        return c ** 2 == a ** 2 + b ** 2

    def name(self):
        return 'Triangle'
