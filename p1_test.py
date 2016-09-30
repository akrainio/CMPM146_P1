import unittest, math
from p1 import navigation_edges


def gen_level(lines):
    walls = set()
    spaces = {}
    waypoints = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == 'X':
                walls.add((x, y))
            elif c.isnumeric():
                spaces[(x, y)] = float(c)
            elif c.islower():
                spaces[(x, y)] = 1.
                waypoints[c] = (x, y)

    level = {'walls': walls,
             'spaces': spaces,
             'waypoints': waypoints}

    return level


class TestStringMethods(unittest.TestCase):
    def test_navigation_edges(self):
        r = math.sqrt(2) * .5
        level_code = ["XXXXX",
                      "X387X",
                      "X217X",
                      "X744X",
                      "XXXXX"]
        level = gen_level(level_code)

        expected = {(1, 1): 4 * r, (2, 1): 4.5, (3, 1): 8 * r,
                    (1, 2): 1.5, (3, 2): 4.0,
                    (1, 3): 8 * r, (2, 3): 2.5, (3, 3): 5 * r}
        navigated_edges = navigation_edges(level, (2, 2))
        actual = {}
        for e in navigated_edges:
            actual[e[0]] = e[1]
        for k in expected:
            self.assertAlmostEqual(expected.get(k), actual.get(k), 14)

    def test_navigation_edges_corner(self):
        r = math.sqrt(2) * .5
        level_code = ["XX",
                      "X34"]
        level = gen_level(level_code)

        expected = {(2, 1): 3.5}
        navigated_edges = navigation_edges(level, (1, 1))
        actual = {}
        for e in navigated_edges:
            actual[e[0]] = e[1]
        for k in expected:
            self.assertAlmostEqual(expected.get(k), actual.get(k), 14)

    def test_navigation_none(self):
        level_code = ["3"]
        level = gen_level(level_code)
        self.assertEqual([], navigation_edges(level, (1, 1)))
        level_none = gen_level([])
        self.assertEqual([], navigation_edges(level, (1, 1)))
