import unittest

from shapes.shape import Shape
from shapes.triangle import Triangle
from shapes.rectangle import Rectangle

class ShapesTest(unittest.TestCase):
    def test_triangle(self):
        t = Triangle(1, 2, 3)
        self.assertEqual(t.perimeter(), 6)
        # self.assertEqual(t.area(), 0) 

    def test_rectangle(self):
        r = Rectangle(2, 4)
        self.assertEqual(r.perimeter(), 12)
        self.assertEqual(r.area(), 8)
        self.assertFalse(r.isSquare())
    
    def test_shape_interface(self):
        self.assertRaises(Exception, Shape)

if __name__ == '__main__':
    unittest.main()
