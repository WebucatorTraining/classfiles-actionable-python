import unittest
import math
from Circle1 import Circle

class TestCircleFunctions(unittest.TestCase):

    def setUp(self):
        self.circle_r = Circle(5, 'r')
        self.circle_d = Circle(10, 'd')
        self.circle_c = Circle(10 * math.pi, 'c')
        self.circle_a = Circle(25 * math.pi, 'a')
    
    # Test circle_r
    def test_circle_radius(self):
        self.assertEqual(self.circle_r.radius, 5)
        self.assertEqual(self.circle_r.diameter, 10)
        self.assertEqual(self.circle_r.circumference, 10 * math.pi)
        self.assertEqual(self.circle_r.area, 25 * math.pi)
    
    # Test circle_d
    def test_circle_diameter(self):
        self.assertEqual(self.circle_d.radius, 5)
        self.assertEqual(self.circle_d.diameter, 10)
        self.assertEqual(self.circle_d.circumference, 10 * math.pi)
        self.assertEqual(self.circle_d.area, 25 * math.pi)
    
    # Test circle_c
    def test_circle_circumference(self):
        self.assertEqual(self.circle_c.radius, 5)
        self.assertEqual(self.circle_c.diameter, 10)
        self.assertEqual(self.circle_c.circumference, 10 * math.pi)
        self.assertEqual(self.circle_c.area, 25 * math.pi)
    
    # Test circle_a
    def test_circle_area(self):
        self.assertEqual(self.circle_a.radius, 5)
        self.assertEqual(self.circle_a.diameter, 10)
        self.assertEqual(self.circle_a.circumference, 10 * math.pi)
        self.assertEqual(self.circle_a.area, 25 * math.pi)
        
if __name__ == '__main__':
    unittest.main()