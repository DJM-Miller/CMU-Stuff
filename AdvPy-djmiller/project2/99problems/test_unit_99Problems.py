"""
unittest for 99Problems
"""

__author__ = "Darrin Miller"

import unittest
from NineNineProblems import probs


class Test_99Problems(unittest.TestCase):
    def test1_probs(self):
        ans = probs(10)
        actual = 99
        self.assertEqual(ans,actual)
    
    def test2_probs(self):
        ans = probs(249)
        actual = 299
        self.assertEqual(ans,actual)

    def test3_probs(self):
        ans = probs(72)
        actual = 99
        self.assertEqual(ans,actual)

    def test4_probs(self):
        ans = probs(0)
        actual = 99
        self.assertEqual(ans,actual)

    def test5_probs(self):
        ans = probs(10078)
        actual = 10099
        self.assertEqual(ans,actual)

    def test6_probs(self):
        ans = probs(148)
        actual = 99
        self.assertEqual(ans,actual)


if __name__ == "__main__":
    unittest.main(verbosity=2)

