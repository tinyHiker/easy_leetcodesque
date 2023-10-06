import unittest
'''
Write a function called averagesOfTuples that takes a tuple of tuples which contain numbers, and returns a tuple containing the average values of the numbers in the provided tuple of tuples.
For example, averagesOfTuples(((2,3,4),(2,32),(1,5,6))) would return (3.0, 17.0, 4.0)
'''

def averagesOfTuples(tupleOfTuples):
    return  tuple([sum(i)/len(i) for i in tupleOfTuples])


class TestTupleMethods(unittest.TestCase):
    def test_averages_of_tuples(self):
        self.assertEqual(averagesOfTuples(((2,3,4),(2,32),(1,5,6))),(3.0, 17.0, 4.0))

    def test_averages_of_tuples2(self):
        self.assertEqual(averagesOfTuples(((5,1,15), (63, 72, 108), (6, 6, 18))), (7.0, 81.0, 10.0))

    def test_averages_of_tuples3(self):
        self.assertEqual(averagesOfTuples(((5, 1, 15, 13, 1), (72, 11, 108,4), (19, 6, 18, 2, 35))), (7.0, 48.75, 16.0))

if __name__ == '__main__':
    unittest.main()