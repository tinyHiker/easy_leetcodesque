#!/usr/bin/python3
import unittest


# --------------------------------------------------------------
# Recursive Function
# --------------------------------------------------------------
def stars(rows):
    '''
    Write a recursive function that takes in the number of rows of stars in the triangle
    and computes the total number of stars.

    Ex.
    *
    **
    ***
    ****

    Input: 4
    Output: 10

    Ex.

    *
    **
    ***
    ****
    *****
    ******

    Input: 6
    Output: 21
    '''
    if rows==0:
        return 0
    else:
        return rows + stars(rows - 1)


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(stars(4), 10)

    def test2(self):
        self.assertEqual(stars(6), 21)

    def test3(self):
        self.assertEqual(stars(0), 0)


if __name__ == '__main__':
    unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------