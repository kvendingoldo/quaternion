# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import unittest
from pyquaternion import Quaternion


class TestQuaternion(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sum_1(self):

        self.assertEqual(3 * 4, 12)

    def test_strings_a_3(self):
        self.assertEqual('a' * 3, 'aaa')


if __name__ == '__main__':
    unittest.main()
