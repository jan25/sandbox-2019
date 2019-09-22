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

    def isEquivalent(self):
        return self.a == self.b and self.b == self.c
    
    def isRightTriangle(self):
        a, b, c = sorted([self.a, self.b, self.c])
        return c ** 2 == a ** 2 + b ** 2
