import unittest

'''
    Given a matrix A, return an ascending sorted list of row index numbers based on the 
    sum of numbers in that row. Assume the sums will be unique.

    A = [
        [1,2,3,4,5],
        [0,0,4,2,3],
        [9,4,3,1,3],
        [0,-3,-7,15,3],
        [7,0,9,9,3],
    ]
    Row sums are:
    Row 0: 15
    Row 1: 9
    Row 2: 20 
    Row 3: 8
    Row 4: 28
    So in ascending order, returns [3,1,0,2,4]
'''


def row_sorter(A):
    matrix_dict= dict({})
    for i in range(len(A)):
        matrix_dict[i]=sum(A[i])

    print(matrix_dict)

    matrix_list= list(zip(matrix_dict.keys(), matrix_dict.values()))


    sorted_matrix_dict= matrix_list.sort(reverse=False, key= lambda x: x[1])

    print(sorted_matrix_dict)


A = [
        [1,2,3,4,5],
        [0,0,4,2,3],
        [9,4,3,1,3],
        [0,-3,-7,15,3],
        [7,0,9,9,3],
    ]
row_sorter(A)

"""
# --------------------------------------------------------------
# The Testing
# # --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(row_sorter([
            [1, 1, 1, 1, 3],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 2],
            [1, 0, 0, 0, 3],
            [1, 0, 0, 0, -10]]
        ), [4, 1, 2, 3, 0])

    def test2(self):
        self.assertEqual(row_sorter([
            [1, 4, 5],
            [0, -3, 0],
            [1, 3, 2]]
        ), [1, 2, 0])

    def test3(self):
        self.assertEqual(row_sorter([
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 2, 11],
            [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0]]
        ), [0, 4, 3, 7, 5, 2, 6, 1])

    def test4(self):
        self.assertEqual(row_sorter([
            [1, 0],
            [0, 2]]
        ), [0, 1])

    def test5(self):
        self.assertEqual(row_sorter([
            [0, 0],
            [1, 1]]
        ), [0, 1])

    def test6(self):
        self.assertEqual(row_sorter([
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 9],
            [1, 1, 2, 1, 1],
            [1, 0, 0, 0, 20]]
        ), [1, 0, 3, 2, 4])


if __name__ == '__main__':
    unittest.main(exit=True)

"""