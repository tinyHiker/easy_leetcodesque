import unittest
'''
    Given a matrix A, count how many rows and columns of all ones there are.

    A = [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1]
    ]
    Returns 3
    2 cols of all 1s and 1 row of all 1s.
'''
def rowcol(A) :
    all_one_count=0
    for i in range(len(A)):
        if sum(A[i])/len(A[i])==1.0:
            all_one_count+=1

    def colTester(A, x):


    for i in range(len(A)):
        for x in range(len(i)):
            







    ### CODE ABOVE ###
    pass

# --------------------------------------------------------------
# The Testing
# # --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(rowcol([
                            [1,1,1,1,1],
                            [1,0,0,0,1],
                            [1,0,0,0,1],
                            [1,0,0,0,1],
                            [1,0,0,0,1]]
                            ), 3)
    def test2(self):
                self.assertEqual(rowcol([
                            [1,1,1],
                            [1,1,1]
                            ]
                            ), 5)
    def test3(self):
                self.assertEqual(rowcol([
                            [1,1,0,0,1,0,0,0,1,1,0],
                            [1,0,0,0,1,0,0,0,1,1,0],
                            [1,0,1,1,1,1,1,0,1,1,0],
                            [1,0,0,0,1,0,1,0,1,1,0],
                            [0,1,0,0,1,0,0,0,1,1,0],
                            [1,1,1,0,1,0,1,0,1,1,0],
                            [1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,0,0,1,0,1,0,1,1,0]]
                            ), 4)
    def test4(self):
                self.assertEqual(rowcol([
                            [0,0],
                            [0,0]]
                            ), 0)
    def test5(self):
                self.assertEqual(rowcol([
                            [1,1],
                            [1,1]]
                            ), 4)
    def test6(self):
        self.assertEqual(rowcol([
                            [1,1,1,1,1],
                            [1,0,0,0,1],
                            [1,0,0,0,1],
                            [1,1,1,1,1],
                            [1,0,0,0,1]]
                            ), 4)

if __name__ == '__main__':
 unittest.main(exit=True)