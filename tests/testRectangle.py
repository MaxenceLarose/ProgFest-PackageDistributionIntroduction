import unittest

from polygon.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def testWhenCreated_shouldDefineItsArea(self):
        rectangle = Rectangle(width=10, height=10)
        self.assertEqual(100, rectangle.area)
