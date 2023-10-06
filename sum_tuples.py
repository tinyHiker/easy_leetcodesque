#!/usr/bin/python3
#DONE
import unittest
# --------------------------------------------------------------
# Recursion: sums of tuples
# --------------------------------------------------------------
def sumtuples(L) :
    '''
    Assumes L is a list of tuples of numbers
    Returns a list of the sums of the tuples, but 
    if L is empty then return []

    CONSTRAINT: YOU MUST USE RECURSION. NO LOOPS. (MARK FOR LOOP IS 0).

    For example, 
    sumtuples([(1, 3, 5), (4, 8, 12, 7), (2, 7)]) returns [9, 31, 9]

    Hint: To get the sum of a tuple t, you can use sum(t)
    '''
    if len(L)==0:
     return []
    else:
     return [sum(L.pop(0))]+sumtuples(L)

def sumtuples1(L):
    '''
    Assumes L is a list of tuples of numbers
    Returns a list of the sums of the tuples, but
    if L is empty then return []

    CONSTRAINT: YOU MUST USE RECURSION. NO LOOPS. (MARK FOR LOOP IS 0).

    For example,
    sumtuples([(1, 3, 5), (4, 8, 12, 7), (2, 7)]) returns [9, 31, 9]

    Hint: To get the sum of a tuple t, you can use sum(t)
    '''
    try:
        return [(sum(L[i])) for i in range(len(L))]
    except TypeError:
        print("Did not enter list of itarables")


print(sumtuples1([(1, 3, 5), (4, 8, 12, 7), 7]))



# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(sumtuples([]), [])
 def test2(self):
  self.assertEqual(sumtuples([(5,)]), [5])
 def test3(self):
  self.assertEqual(sumtuples([(1, 3, 5), (4, 8, 12, 7), (2, 7)]), [9, 31, 9])
 def test4(self):
  self.assertEqual(sumtuples([(), (), (5,), (1, 2, 3, 4, 5)]), [0, 0, 5, 15])

if __name__ == '__main__':
 unittest.main(exit=True)




# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
