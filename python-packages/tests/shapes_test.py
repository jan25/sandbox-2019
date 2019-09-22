import unittest

from shapes.shape import Shape
from shapes.triangle import Triangle
from shapes.rectangle import Rectangle

class ShapesTest(unittest.TestCase):
    def test_triangle(self):
        t = Triangle(3, 2, 3)
        self.assertEqual(t.perimeter(), 8)
        self.assertLess(abs(t.area() - 2.828427), 0.000001)

    def test_rectangle(self):
        r = Rectangle(2, 4)
        self.assertEqual(r.perimeter(), 12)
        self.assertEqual(r.area(), 8)
        self.assertFalse(r.is_square())
    
    def test_shape_interface(self):
        self.assertRaises(Exception, Shape)

if __name__ == '__main__':
    unittest.main()
