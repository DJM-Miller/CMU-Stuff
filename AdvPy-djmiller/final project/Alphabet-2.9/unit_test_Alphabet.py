"""
unittest for Alphabet
"""

__author__ = "Darrin Miller"

import unittest
from Alphabet import LIS, Alphabet

class Test_Alphabet(unittest.TestCase):
    def test1_LIS(self):
        ans = 23
        with open('1.in') as f:
            ins = f.readline()
        my_ans = LIS(ins)
        self.assertEqual(ans,my_ans)

    def test2_LIS(self):
        ans = 6
        with open('2.in') as f:
            ins = f.readline()
        my_ans = LIS(ins)
        self.assertEqual(ans,my_ans)

    def test3_LIS(self):
        ans = 8
        my_ans = LIS("satguhvgwaxcytzhd")
        self.assertEqual(ans,my_ans)

    def test1_Alphabet(self):
        with open('1.ans') as f:
            ans = int(f.readline())
        with open('1.in') as f:
            ins = f.readline()
        my_ans = Alphabet(ins)
        self.assertEqual(ans,my_ans)

    def test2_Alphabet(self):
        with open('2.ans') as f:
            ans = int(f.readline())
        with open('2.in') as f:
            ins = f.readline()
        my_ans = Alphabet(ins)
        self.assertEqual(ans,my_ans)

    def test3_Alphabet(self):
        ans = 18
        ins = "satguhvgwaxcytzhd"
        my_ans = Alphabet(ins)
        self.assertEqual(ans,my_ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)