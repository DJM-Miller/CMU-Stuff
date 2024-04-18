"""
unittest for Howl
"""

__author__ = "Darrin Miller"

import unittest
from Howl import howlBack

class Test_Howl(unittest.TestCase):
    def test1_howlBack(self):
        howl_len = 5
        ans = howlBack(howl_len)
        self.assertGreater(len(ans),howl_len) #Assert that the howl back is longer than incoming howl
    
    def test2_howlBack(self):
        howl_len = len("AHOW")
        ans = howlBack(howl_len)
        self.assertGreater(len(ans),howl_len)

    def test3_howlBack(self):
        howl_len = len("AAHOOW")
        ans = howlBack(howl_len)
        self.assertGreater(len(ans),howl_len)

    def test4_howlBack(self):
        howl_len = 125
        ans = howlBack(howl_len)
        self.assertGreater(len(ans),howl_len)

    def test5_howlBack(self):
        howl_len = len("AAHOOWO")
        ans = howlBack(howl_len)
        self.assertGreater(len(ans),howl_len)
    
    def test6_howlBack(self):
        howl_len = 4
        ans = howlBack(howl_len)
        self.assertGreater(len(ans),howl_len)
        

if __name__ == "__main__":
    unittest.main(verbosity=2)