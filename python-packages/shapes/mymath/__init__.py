'''
Square root of a floating point number upto 6 decimal places
This def uses Newton Raphsons method

Args:
f   can be a int or float
err use to set custom approximation error
default is upto 6 decimal places

Returns:
square root of given float f
'''
def sqrt(f, err=0.000001):
    s = 1.0
    while abs(f / s - s) > err:
        s = (f + s * s) / (2 * s)
    return s
