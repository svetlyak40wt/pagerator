#!/usr/bin/env python

import unittest
from pagerator import IterableQuery

class Tests(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        super(Tests, self).setUp(*args, **kwargs)

        self.hits = []
        def getter(page):
            self.hits.append(page)
            if page == 0:
                return range(0, 10)
            elif page == 1:
                return range(10, 20)
            return []

        self.obj = IterableQuery(getter = getter, page_size = 10)

    def test_chaining(self):
        self.assertEqual(range(0, 20), list(self.obj))

    def test_limiting(self):
        self.assertEqual(range(0, 5), list(self.obj[:5]))
        self.assertEqual(range(5, 20), list(self.obj[5:]))
        self.assertEqual(range(3, 5), list(self.obj[3:5]))
        self.assertEqual(range(5, 15), list(self.obj[5:15]))

    def test_sublimiting(self):
        self.assertEqual(range(5, 15), list(self.obj[:15][5:]))
        self.assertEqual(range(7, 15), list(self.obj[5:15][2:20]))
        self.assertEqual(range(7, 17), list(self.obj[5:30][2:10]))

    def test_skip_pages(self):
        self.assertEqual(range(15, 17), list(self.obj[15:17]))
        self.assertEqual([1], self.hits)

    def test_infinite_loop(self):
        self.assertEqual([], list(self.obj[0:0]))
        self.assertEqual([], self.hits)


if __name__ == '__main__':
    unittest.main()

