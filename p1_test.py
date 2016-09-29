import unittest, math
from p1 import navigation_edges


class TestStringMethods(unittest.TestCase):

    def test_navigation_edges(self):
        r2 = math.sqrt(2)
        spaces = {(0,0): 2,    (1,0): 2,    (2,0): 2,    (3,0): 2,    (4,0): 2,
                  (0,1): 2,    (1,1): r2*1, (2,1): r2*2, (3,1): r2*9, (4,1): 2,
                  (0,2): 2,    (1,2): r2*8, (2,2): r2*4, (3,2): r2*4, (4,2): 2,
                  (0,3): 2,    (1,3): r2*9, (2,3): r2*6, (3,3): r2*1, (4,3): 2,
                  (0,4): 2,    (1,4): 2,    (2,4): 2,    (3,4): 2,    (4,4): 2}
        level = {'spaces': spaces}
        expected = {(1,1): 5.0,    (2,1): r2*3.0, (3,1): 13.0,
                    (1,2): r2*6.0,                (3,2): r2*4,
                    (1,3): 13.0,   (2,3): r2*5.0, (3,3): 5.0}
        navigated_edges = navigation_edges(level, (2,2))
        navdict = {}
        for e in navigated_edges:
            navdict[e[0]] = e[1]
        for k in expected:
            self.assertAlmostEqual(expected.get(k), navdict.get(k), 14)

    def test_navigation_edges_corner(self):
        r2 = math.sqrt(2)
        spaces = {(0, 0): r2*1, (1, 0): r2*3, (2, 0): 2,
                  (0, 1): r2*5, (1, 1): r2*4, (2, 1): r2*2,
                  (0, 2): 2,    (1, 2): r2*8, (2, 2): r2*4}
        level = {'spaces': spaces}
        expected = {                (1, 0): r2*2.0,
                    (0, 1): r2*3.0, (1, 1): 5.0}
        navigated_edges = navigation_edges(level, (0, 0))
        navdict = {}
        for e in navigated_edges:
            navdict[e[0]] = e[1]
        for k in expected:
            self.assertAlmostEqual(expected.get(k), navdict.get(k), 14, "" + k.__str__() + ": expected: " + expected.get(k).__str__()
                                   + ", got: " + str(navdict.get(k)))

    def test_navigation_none(self):
        spaces = {(0, 0): 1, (1, 0): 3, (2, 0): 2,
                  (0, 1): 5, (1, 1): 4, (2, 1): 2,
                  (0, 2): 2, (1, 2): 8, (2, 2): 4}
        level = {'spaces': spaces}
        self.assertEqual([], navigation_edges(level, (9, 9)))
        spaces = {}
        level.update(spaces)
        self.assertEqual([], navigation_edges(level, (9, 9)))
