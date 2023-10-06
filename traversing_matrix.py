#DONE
import unittest
"""
2D arrays

Return a tuple with the row and column coordinates of
the smallest element in the matrix.

Example:
A = [[1, 2], [-99, 4], [5, 6]]
result = (1,0)    since -99 is the smallest element.
"""

# --------------------------------------------------------------
# Your implementation: 
# --------------------------------------------------------------
def find_smallest(matrix) :
    # YOUR CODE GOES HERE
    smallest=matrix[0][0]
    smallest_cor= (0,0)

    for i in range(len(matrix)):
      for x in range(len(matrix[i])):
        if matrix[i][x]<=smallest:
          smallest=matrix[i][x]
          smallest_cor= (i,x)

    return smallest_cor

def return_smallest(matrix):
    return min([min(i) for i in matrix])


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
  def test1(self):
    A = [[1, 2], [-99, 4], [5, 6]]
    self.assertEqual(find_smallest(A), (1,0))
  def test2(self):
    A = [[1, -9999999999999999], [-99, 4], [5, 6]]
    self.assertEqual(find_smallest(A), (0,1))
  def test3(self):
    A = [[10, 59], [0.2, 88], [4, 0.1]]
    self.assertEqual(find_smallest(A), (2,1))
  def test4(self):
    A = [[-10, -59, -3], [-0.2, -88, -4], [-4, -0.1, -5]]
    self.assertEqual(find_smallest(A), (1,1))
  def test5(self):
    A = [[-10], [-0.2], [-400],[-200]]
    self.assertEqual(find_smallest(A), (2,0))
  def test6(self):
    A = [[1,2,3],[4,5,6]]
    self.assertEqual(return_smallest(A), 1)

          
if __name__ == '__main__':
  unittest.main(exit=True)
 
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
