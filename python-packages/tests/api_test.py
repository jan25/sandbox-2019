import unittest

from api.geometry import GeometricShape

class ApiTest(unittest.TestCase):
    def test_triangle_shape(self):
        t = GeometricShape(1, 2, 3)
        self.assertEqual(t.perimeter(), 6)
        self.assertEqual(t.name(), "<class 'shapes.triangle.Triangle'>")

    def test_rectangle_shape(self):
        r = GeometricShape(2, 4)
        self.assertEqual(r.area(), 8)
        self.assertEqual(r.perimeter(), 12)
        self.assertEqual(r.name(), "<class 'shapes.rectangle.Rectangle'>")

    def test_invalid_shape(self):
        r = GeometricShape(1)
        self.assertRaises(AssertionError, r.area)
        self.assertRaises(AssertionError, r.perimeter)

if __name__ == '__main__':
    unittest.main()
