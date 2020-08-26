import unittest
from Die2 import Die

class TestDieFunctions(unittest.TestCase):

    def setUp(self):
        self.die1 = Die()
        self.die2 = Die(8)
    
    def test_init(self):
        self.assertEqual(self.die1.sides, 6)
        self.assertEqual(self.die2.sides, 8)
        
if __name__ == '__main__':
    unittest.main()