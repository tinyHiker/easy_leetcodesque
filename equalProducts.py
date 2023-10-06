import unittest
'''
Write a function called equalProducts which takes in a tuple and checks if there is a position in the tuple 
which splits the tuple into two sections such that the product of the left section is equal to the product of the right section.
If such a position exists, the function returns a list containing two tuples, the first tuple is the left section, and the second tuple
is the right section. If such a position does not exist, return False. 
Example:
equalProducts((6,7,8,7,8,6)) -> [(6,7,8),(7,8,6)]
equalProducts((18,3,3,2)) -> [(18,),(3,3,2)]
equalProducts((18,6,3,2)) -> False
'''
import math

def equalProducts(numberTuple):

    splitPoint=0
    splitEqual= False
    for i in range(len(numberTuple)):
        if math.prod(numberTuple[:i])== math.prod(numberTuple[i:]):
            splitPoint=i
            splitEqual= True
            break
    if splitEqual==False:
        return False
    else:
        return [numberTuple[:i], numberTuple[i:]]





class TestTupleMethods(unittest.TestCase):

    def test_equal_products(self):
        self.assertEqual(equalProducts((6,7,8,7,8,6)),[(6, 7, 8), (7, 8, 6)])

    def test_equal_products2(self):
        self.assertEqual(equalProducts((18,3,3,2)),[(18,),(3,3,2)])

    def test_equal_products3(self):
        self.assertEqual(equalProducts((18,6,3,2)),False)

if __name__ == '__main__':
    unittest.main()