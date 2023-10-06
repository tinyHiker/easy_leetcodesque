import unittest
'''
For this question, you have been tasked with determining which students from a high school are eligible for a 
scholarship to your university. In order to be eligible, a student must have won at least 3 student of the month awards
in the past 12 months. You are given a list containing the names of the student of the month winners for each of the past 
12 months. Write a function called eligibleStudents that takes this list and returns a new list containing only the 
names of the eligible students. The names in the returned list should be in the same order that they appear in the 
original list (See test cases).   

For example: eligibleStudents(["John", "Mary", "Steve", "John", "John", "Matt", "Matt", "Steve", "Steve", "Mary", "Steve"]) ----> ['John', 'Steve']. 
'''

def eligibleStudents(winners):
    awards_dict= dict(zip(winners, [winners.count(i) for i in winners]))
    eledge_list= [i for i in awards_dict.keys() if awards_dict[i]>=3]

    return eledge_list


class TestDictMethods(unittest.TestCase):
    def test_eligible_students(self):
        self.assertEqual(eligibleStudents(["John", "Mary", "Steve", "John", "John", "Matt", "Matt", "Steve", "Steve", "Mary", "Steve", "Jessica"]), ['John', 'Steve'])
    def test_eligible_students2(self):
        self.assertEqual(eligibleStudents(["Henry", "Mary", "Steve", "John", "John", "Matt", "Matt", "Steve", "Henry", "Mary", "Susan", "Susan"]), [])
    def test_eligible_students3(self):
        self.assertEqual(eligibleStudents(["John", "Mary", "Mary", "John", "John", "Matt", "Matt", "Steve", "Steve", "Mary", "Steve", "Matt"]), ['John', 'Mary', 'Matt', 'Steve'])

if __name__ == '__main__':
    unittest.main()