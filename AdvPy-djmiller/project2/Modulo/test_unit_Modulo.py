"""
unittest for Modulo
"""

__author__ = "Darrin Miller"

import unittest
from Modulo import uniqueModulo

class Test_Modulo(unittest.TestCase):
    def test1_uniqueModulo(self):
        actual = 10
        ans = uniqueModulo([1,3,4,5,10,15,16,12,14,17])
        self.assertEqual(ans,actual)

    def test2_uniqueModulo(self):
        actual = 1
        ans = uniqueModulo([42,42,42,42,42,42,42,42,42,42])
        self.assertEqual(ans,actual)
    
    def test3_uniqueModulo(self):
        actual = 1
        ans = uniqueModulo([42,42,42,42,0,0,0,0,0,0])
        self.assertEqual(ans,actual)

    def test4_uniqueModulo(self):
        actual = 1
        ans = uniqueModulo([126,42,42,0,0,0,0,84,84,84])
        self.assertEqual(ans,actual)
    
    def test5_uniqueModulo(self):
        actual = 3
        ans = uniqueModulo([42,42,42,0,0,0,1,1,19,84])
        self.assertEqual(ans,actual)

    def test6_uniqueModulo(self):
        actual = 4
        ans = uniqueModulo([42,-42,42,-42,42,2,12,62,54,42])
        self.assertEqual(ans,actual)

    
        





if __name__ == "__main__":
    unittest.main(verbosity=2)