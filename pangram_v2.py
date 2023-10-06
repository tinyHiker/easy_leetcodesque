
import unittest

'''
    There are special types of sentences called "pangrams" which contain every
    letter of the alphabet at least once. We'd like to extend this idea and
    check for sentences which also contain every digit and at least one space.
    Case insensitive, meaning "A" is considered the same as "a".

    Given a string s which contains only letters, digits, or spaces,
    write a function which checks if a string contains at least one of every
    letter in the alphabet, at least one of each digit, and at least one space.

    ex:
    s = "The 1 2quic0k b7rown5 fo6x jumps3 over4 t8he lazy dog9"
    Returns True (contains all letters and all digits)

    s = "The f11ive boxing wiz6ards ju9mp qu0ickly.!4"
    Returns False (missing digits)
'''


def pangram_v2(s):

    s= s.lower()
    string_list= list(s)

    zeros_list= [0 for i in string_list]

    string_dict= dict(zip(string_list, zeros_list))

    for i in string_dict:
        string_dict[i]= string_list.count(i)

    checkerList = tuple('abcdefghijklmnopqrstuvwxyz0123456789 ')

    allOverZero= True
    for i in string_dict.values():
        if i==0:
            allOverZero=False


    if checkerList in string_dict.keys() and allOverZero==True:
        return True
    else:
        return False




# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    

    def test2(self):
        self.assertEqual(pangram_v2("The f11ive boxing wiz6ards ju9mp qu0ickly.4"), False)

    def test3(self):
        self.assertEqual(pangram_v2("gh9g824hg982gbjnkdbqviwbffiadasd"), False)

    def test4(self):
        self.assertEqual(pangram_v2("0123456789abcdef"), False)

    def test5(self):
        self.assertEqual(pangram_v2(''), False)


if __name__ == '__main__':
    unittest.main(exit=True)


