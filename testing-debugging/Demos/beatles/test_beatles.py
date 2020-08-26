import unittest
import beatles

class TestBeatles(unittest.TestCase):

    def setUp(self):
        print('Setting up')
        self.beatles = beatles.Beatles()
        self.beatles.create()
        self.beatles.insert()

    def tearDown(self):
        print('Tearing down')
        self.beatles.close()
    
    def test_select(self):
        query = 'SELECT * FROM beatles'
        result = self.beatles.select(query)
        self.assertIsInstance(result, list)
    
    def test_select_one(self):
        query = "SELECT * FROM beatles"
        result = self.beatles.select_one(query)
        self.assertIsInstance(result, tuple)

if __name__ == '__main__':
    unittest.main()