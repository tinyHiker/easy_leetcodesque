#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Write a recursive function that adds a "|" between adjacent characters
# --------------------------------------------------------------
def addBar(word) :
    '''
    Ex.
    Input: "Water"
    Output: "W|a|t|e|r"
    '''
    if len(word)==0:
        return ""
    elif len(word)==1:
        return word[-1]
    else:
        return word[0] + "|" + addBar(word[1:])

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(addBar("3.14"), "3|.|1|4")
 def test2(self):
  self.assertEqual(addBar("AppleJuice"), "A|p|p|l|e|J|u|i|c|e")
 def test3(self):
  self.assertEqual(addBar(""),"")

if __name__ == '__main__':
 unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------