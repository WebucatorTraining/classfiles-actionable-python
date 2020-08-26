import unittest
from functions_error import prepend, append, insert

class TestMyMethods(unittest.TestCase):
    def test_prepend(self):
        self.assertEqual(prepend('bar', 'foo'), 'foobar')
    def test_append(self):
        self.assertEqual(append('bar', 'foo'), 'barfoo')
    def test_insert(self):
        self.assertEqual(insert('wetor', 'buca', 2), 'webucator')

if __name__ == '__main__':
    unittest.main()