#!/usr/bin/python3
import unittest


# --------------------------------------------------------------
def find_root3(x, epsilon):
    '''
    Assume: x, epsilon are floating point numbers and epsilon > 0
    Use bisection search to find the following root of x such that
    If x >=0, return y such that x - epsilon <= y ** 4 <= x + epsilon
    Else, return y such that x - epsilon <= y ** 3 <= x + epsilon

    Note: You must use bisection search to implement the function.
    '''
    # YOUR CODE GOES HERE
    h = max(1.0, x)
    l = 0.0

    y = (h + l) / 2.0
    if x>=0:
        while not(x - epsilon <= y ** 4 <= x + epsilon):
            if y ** 4 < x:
                l = y
            else:
                h = y

            y = (h + l) / 2.0
        return y

    elif x<0:
        while not(x - epsilon <= y ** 3 <= x + epsilon):
            if y ** 3 < x:
                h = y
            else:
                l = y

            y = (h + l) / 2.0


        return y

find_root3(16,0.1)
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        x, epsilon = 0.0, 0.0001
        y = find_root3(x, epsilon)
        if y == None:
            error = 10*epsilon
        else:
            error = abs(y ** 4 - x)
        self.assertTrue(error <= epsilon)

    def test2(self):
        x, epsilon = -50.0, 0.001
        y = find_root3(x, epsilon)
        if y == None:
            error = 10*epsilon
        else:
            error = abs(y ** 3 - x)
        self.assertTrue(error <= epsilon)
        self.assertFalse(error <= epsilon / 100)

    def test3(self):
        x, epsilon = -0.5, 0.001
        y = find_root3(x, epsilon)
        if y == None:
            error = 10*epsilon
        else:
            error = abs(y ** 3 - x)
        self.assertTrue(error <= epsilon)
        self.assertFalse(error <= epsilon / 100)

    def test4(self):
        x, epsilon = 2.0, 0.001
        y = find_root3(x, epsilon)
        if y == None:
            error = 10*epsilon
        else:
            error = abs(y ** 4 - x)
        self.assertTrue(error <= epsilon)
        self.assertFalse(error <= epsilon / 100)

    def test5(self):
        x, epsilon = 0.3, 0.001
        y = find_root3(x, epsilon)
        if y == None:
            error = 10*epsilon
        else:
            error = abs(y ** 4 - x)
        self.assertTrue(error <= epsilon)
        self.assertFalse(error <= epsilon / 100)


if __name__ == '__main__':
    unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
