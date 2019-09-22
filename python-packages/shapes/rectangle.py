'''
.. module:: rectangle

Rectangle shape implementation. This shape has a length and a bredth.
'''
class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b
    
    def perimeter(self):
        return 2 * (self.l + self.b)
    
    def area(self):
        return self.l * self.b
    
    def is_square(self):
        '''
        Use this to check if Rectangle is a valid square

        :returns: bool -- if rectangle is square
        '''
        return self.l == self.b

    def name(self):
        return 'Rectangle'
