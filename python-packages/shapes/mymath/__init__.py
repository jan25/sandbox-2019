
'''
Square root of a floating point number
using Newton Raphons approximation
use err argument to set custom approximation error
'''
def sqrt(f, err=0.000001):
    s = 1.0
    while (abs(f / s - s) > err):
        s = (s + f / s) / 2.0
    return s
