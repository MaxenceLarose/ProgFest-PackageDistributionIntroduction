import unittest

from polygon.quadrilateral import Quadrilateral


class TestRectangle(unittest.TestCase):
    def testWhenCreated_shouldDefineItsArea(self):
        quad = Quadrilateral(width=10, height=10)
        self.assertEqual(100, quad.area)
