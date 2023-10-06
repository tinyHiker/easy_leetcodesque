#!/usr/bin/python3
import unittest
# --------------------------------------------------------------e131
# Review: condition, loop, approximation, STRING, list, dict, recursion, 
# 2D, exception, class
# --------------------------------------------------------------
def q4(s) :
    '''
    Assumes s is a string.
    Returns a new string formed by concatenating i copies of the letter 
    at position i, for each index position in string s.
    For example, 
    q4('dog') returns 'ogg'   since 0 of 'd' and 1 of 'o' and 2 of 'g'
    '''
    newString=""
    for i in range(len(s)):
        for z in range(i):
            newString= newString+s[i]
    return newString

# --------------------------------------------------------------
# TEST CASES
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(q4('dog'), 'ogg')
    def test1(self):
        self.assertEqual(q4('horse'), 'orrssseeee')
    def test2(self):
        self.assertEqual(q4('b'), '')
    def test3(self):
        self.assertEqual(q4('hippotamus'), 'ipppppooootttttaaaaaammmmmmmuuuuuuuusssssssss')

if __name__=='__main__':
    unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
