import unittest, math
from p1 import navigation_edges


class TestStringMethods(unittest.TestCase):

    def test_navigation_edges(self):
        r2 = math.sqrt(2)
        spaces = {(0,0): 2,    (1,0): 2,    (2,0): 2,    (3,0): 2,    (4,0): 2,
                  (0,1): 2,    (1,1): r2*1, (2,1): 2,    (3,1): r2*9, (4,1): 2,
                  (0,2): 2,    (1,2): 8,    (2,2): r2*4, (3,2): r2*4,    (4,2): 2,
                  (0,3): 2,    (1,3): r2*9, (2,3): 6,    (3,3): r2*1, (4,3): 2,
                  (0,4): 2,    (1,4): 2,    (2,4): 2,    (3,4): 2,    (4,4): 2}
        level = {'spaces': spaces}
        expected = [((1,1),2.5), ((2,1),3.0), ((3,1),6.5),
                    ((1,2),6.0),              ((3,2),r2*4),
                    ((1,3),6.5), ((2,3),5.0), ((3,3),2.5)]
        print(navigation_edges(level, (2,2)))
        self.assertEqual(expected, navigation_edges(level, (2,2)))
