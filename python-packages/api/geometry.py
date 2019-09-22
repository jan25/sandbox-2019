from shapes.rectangle import Rectangle
from shapes.triangle import Triangle

class GeometricShape:
    def __init__(self, *sides):
        self.sides = sides
        self.shape = None
        self._init()
    
    def _init(self):
        self.n = len(self.sides)
        assert (self.n < 4), 'No support for sides > 3'
        if self.n == 3:
            self.shape = Triangle(*self.sides)
        elif self.n == 2:
            self.shape = Rectangle(*self.sides)
    
    def name(self):
        self._assert_shape()
        return self.shape.name()

    def perimeter(self):
        self._assert_shape()
        return self.shape.perimeter()
    
    def area(self):
        self._assert_shape()
        return self.shape.area()

    def _assert_shape(self):
        assert (self.shape is not None), 'Not a valid geometric shape'
