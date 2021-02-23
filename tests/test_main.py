import unittest
from main import reading_tiffs


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pass

    def test_reading_tiff(self):
        """ Not sure how tiffs work but this wold be the unit test for it. """
        t = reading_tiffs()
        pass


if __name__ == '__main__':
    unittest.main()
