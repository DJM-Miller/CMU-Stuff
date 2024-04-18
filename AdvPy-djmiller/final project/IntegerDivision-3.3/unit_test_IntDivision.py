"""
unittest for IntegerDivision
"""

__author__ = "Darrin Miller"

import unittest
import sys
from IntegerDivision import intDivision, get_input

class Test_IntegerDivision(unittest.TestCase):
    def test1_intDiv(self):
        with open('1.ans') as f:
            ans = int(f.readline())
        sys.stdin = open("1.in","r")
        d,L = get_input()
        my_ans = intDivision(d,L)
        self.assertEqual(ans,my_ans)
        sys.stdin.close()

    def test2_intDiv(self):
        with open('2.ans') as f:
            ans = int(f.readline())
        sys.stdin = open("2.in","r")
        d,L = get_input()
        my_ans = intDivision(d,L)
        self.assertEqual(ans,my_ans)
        sys.stdin.close()

    def test3_intDiv(self):
        with open('3.ans') as f:
            ans = int(f.readline())
        sys.stdin = open("3.in","r")
        d,L = get_input()
        my_ans = intDivision(d,L)
        self.assertEqual(ans,my_ans)
        sys.stdin.close()

    def test4_intDiv(self):
        ans = 6
        my_ans = intDivision(3, [0,1,2,3,4,5])
        self.assertEqual(ans,my_ans)

    def test5_intDiv(self):
        ans = 3
        my_ans = intDivision(3, [0,1,3,4,6,7])
        self.assertEqual(ans,my_ans)
    
    def test6_intDiv(self):
        ans = 15
        my_ans = intDivision(10, [0,1,2,3,4,5])
        self.assertEqual(ans,my_ans)

if __name__ == "__main__":
    unittest.main(verbosity=2)