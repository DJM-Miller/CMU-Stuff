"""
unittest for ADifferentProblem
"""

__author__ = "Darrin Miller"

import unittest
from ADifferentProblem import findDifference

class Test_Howl(unittest.TestCase):
    def test1_findDifference(self):
        actual = 3
        ans = findDifference(10, 13)
        self.assertEqual(ans,actual)
    def test2_findDifference(self):
        actual = 3
        ans = findDifference(13, 10)
        self.assertEqual(ans,actual)
    def test3_findDifference(self):
        actual = 0
        ans = findDifference(10, 10)
        self.assertEqual(ans,actual)
    def test4_findDifference(self):
        actual = 0
        ans = findDifference(0, 0)
        self.assertEqual(ans,actual)
    def test5_findDifference(self):
        actual = 2
        ans = findDifference(1234567892, 1234567894)
        self.assertEqual(ans,actual)
    def test6_findDifference(self):
        actual = 100000000000000000
        ans = findDifference(987654321123456789, 887654321123456789)
        self.assertEqual(ans,actual)


if __name__ == "__main__":
    unittest.main(verbosity=2)