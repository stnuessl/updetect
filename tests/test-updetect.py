#!/usr/bin/env python

import os
import tempfile
import unittest

import updetect


class FindTester(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFindArgPaths001(self):
        tests = [
            (
                __file__,
                [__file__]
            ),
            (
                [__file__],
                [__file__]
            ),
            (
                os.path.dirname(__file__),
                [__file__]
            ),
            (
                f'{os.path.dirname(__file__)}/../tests',
                [__file__]
            ),
            (
                f'{os.path.dirname(__file__)}/',
                [__file__]
            ),
            (
                f'{os.path.dirname(__file__)}///',
                [__file__]
            ),
            (
                [__file__, os.path.dirname(__file__)],
                [__file__, __file__]
            ),
        ]

        for paths, expected in tests:
            results = updetect.find(paths, '*.py', recursive=False)

            self.assertEqual(expected, results)


    def testFindArgNames001(self):
        tests = [
            (
                __file__,
                [__file__]
            ),
            (
                '*.py',
                [__file__]
            ),
            (
                '*.*',
                [__file__, f'{os.path.splitext(__file__)[0]}.sh' ]
            ),
            (
                '[!_]*[!_]',
                [__file__, f'{os.path.splitext(__file__)[0]}.sh' ]
            ),
            (
                '*.c',
                []
            ),
            (
                ['*.py', '*.h'],
                [__file__]
            ),
        ]

        for pattern, expected in tests:
            results = updetect.find(__file__, pattern, recursive=False)

            self.assertEqual(sorted(expected), sorted(results))


    def testFindArgRecursive001(self):
        tests = [
            (
                False,
                lambda x: self.assertEqual(2, len(x))
            ),
            (
                True,
                lambda x: self.assertLess(2, len(x))
            ),
        ]

        for recursive, check_asserts in tests:
            values = updetect.find(__file__, '[!_]*[!_]', recursive)

            check_asserts(values)

    def testArgLimit001(self):
        tests = [
            ( 0, 0 ),
            ( 1, 1 ),
            ( -1, 1 ),
            ( -2, 1 ),
        ]

        for limit, expected in tests:
            results = updetect.find(__file__,
                                    __file__,
                                    recursive=False,
                                    limit=limit)

            self.assertEqual(expected, len(results))

    def testFind001(self):
        tests = [
            (
                __file__,
                'README.rst',
                True,
                1,
                lambda x: (
                    self.assertEqual(1, len(x)),
                    self.assertEqual('README.rst', os.path.basename(x[0]))
                )
            ),
            (
                os.path.dirname(__file__),
                ['tests/*.py'],
                True,
                1,
                lambda x: (
                    self.assertEqual(1, len(x)),
                    self.assertEqual(__file__, x[0])
                )
            ),
            (
                f'{os.path.dirname(__file__)}/..',
                'tests/*.py',
                True,
                1,
                lambda x: (
                    self.assertEqual(1, len(x)),
                    self.assertEqual(__file__, x[0])
                )
            ),
        ]

        for paths, names, recursive, limit, check_asserts in tests:
            results = updetect.find(paths, names, recursive, limit)

            check_asserts(results)


if __name__ == '__main__':
    unittest.main()
