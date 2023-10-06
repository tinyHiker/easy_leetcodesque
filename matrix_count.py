import unittest
'''
    Given a matrix A, count the amount of 2x2 squares in the matrix.
    1 represents part of a square, 0 represents nothing. Assume A is at least
    of size 2 by 2.

    ex:
    A = [
        [1,1,1],
        [1,1,1]
    ]
    Returns 2

    A = [
        [1,1,0,0,1],
        [1,1,0,0,1],
        [1,1,1,1,1],
        [1,0,1,0,1],
        [1,1,1,0,1]
    ]
    Returns 2
'''
def square(A) :
    squareCount=0
    for i in range(len(A)-1):
        for x in range(len(A[i])-1):
            if A[i][x]==1 and A[i][x+1]==1 and A[i+1][x]==1 and A[i+1][x+1]==1:
                squareCount+=1

    return squareCount




    

# --------------------------------------------------------------
# The Testing
# # --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(square([
                            [1,1,0,0,1],
                            [1,1,0,0,1],
                            [1,1,1,1,1],
                            [1,0,1,0,1],
                            [1,1,1,0,1]]
                            ), 2)
    def test2(self):
                self.assertEqual(square([
                            [1,1,1],
                            [1,1,1]
                            ]
                            ), 2)
    def test3(self):
                self.assertEqual(square([
                            [1,1,0,0,1,0,0,0,1,1,0],
                            [1,0,0,0,1,0,0,0,1,1,0],
                            [1,0,1,1,1,1,1,0,1,1,0],
                            [1,0,0,0,1,0,1,0,1,1,0],
                            [0,1,0,0,1,0,0,0,1,1,0],
                            [1,1,1,0,1,0,1,0,1,1,0],
                            [1,1,0,1,1,0,1,0,1,1,0],
                            [1,1,0,0,1,0,1,0,1,1,0]]
                            ), 9)
    def test4(self):
                self.assertEqual(square([
                            [0,0],
                            [0,0]]
                            ), 0)
    def test5(self):
                self.assertEqual(square([
                            [1,1],
                            [1,1]]
                            ), 1)

if __name__ == '__main__':
 unittest.main(exit=True)