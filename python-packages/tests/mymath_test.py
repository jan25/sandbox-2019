import unittest

import shapes.mymath as mymath

class MyMathTest(unittest.TestCase):
    def test_sqrt(self):
        n = 121
        s = mymath.sqrt(n, 0.00000001)
        self.assertLess(abs(s - 11), 0.00000001)
