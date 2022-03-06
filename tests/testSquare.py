import unittest

from polygon.square import Square


class TestRectangle(unittest.TestCase):
    def testWhenCreated_shouldDefineItsArea(self):
        square = Square(side_length=10)
        self.assertEqual(100, square.area)
