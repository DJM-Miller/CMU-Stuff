"""
unittest for Perket
"""

__author__ = "Darrin Miller"

import unittest
import sys
from Perket import Perket, get_ingredients

class Test_Perket(unittest.TestCase):
    def test1_Perket(self):
        with open('perket.1.ans') as f:
            ans = int(f.readline())
        sys.stdin = open("perket.1.in","r")
        my_ans = Perket(get_ingredients())
        self.assertEqual(ans,my_ans)
        sys.stdin.close()
    
    def test2_Perket(self):
        with open('perket.2.ans') as f:
            ans = int(f.readline())
        sys.stdin = open("perket.2.in","r")
        my_ans = Perket(get_ingredients())
        self.assertEqual(ans,my_ans)
        sys.stdin.close()

    def test3_Perket(self):
        with open('perket.3.ans') as f:
            ans = int(f.readline())
        sys.stdin = open("perket.3.in","r")
        my_ans = Perket(get_ingredients())
        self.assertEqual(ans,my_ans)
        sys.stdin.close()

    def test4_Perket(self):
        ans = 2
        my_ans = Perket([(4,7),(4,7)])
        self.assertEqual(ans,my_ans)

    def test5_Perket(self):
        ans = 8
        my_ans = Perket([(1,9)])
        self.assertEqual(ans,my_ans)

    def test6_Perket(self):
        ans = 1
        my_ans = Perket([(4,9),(2,7),(2,1)])
        self.assertEqual(ans,my_ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)