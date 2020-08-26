import unittest
from math_functions import *

class TestMathFunctions(unittest.TestCase):
    
    def test_round_down(self):
        self.assertEqual(round_down(1.3), 1)
        self.assertEqual(round_down(-1.3), -2)
        self.assertEqual(round_down(1.7), 1)
        self.assertEqual(round_down(-1.7), -2)
        self.assertEqual(round_down(0), 0)
        
    def test_round_up(self):
        self.assertEqual(round_up(1.3), 2)
        self.assertEqual(round_up(-1.3), -1)
        self.assertEqual(round_up(1.7), 2)
        self.assertEqual(round_up(-1.7), -1)
        self.assertEqual(round_up(0), 0)
        
if __name__ == '__main__':
    unittest.main()