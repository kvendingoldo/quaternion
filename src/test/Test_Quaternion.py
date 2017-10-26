# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import unittest
from quaternion.Quaternion import Quaternion
from pyquaternion import Quaternion as pyQuaternion


class TestQuaternion(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_1(self):
        q1 = Quaternion.random()
        q2 = pyQuaternion(q1.get_turtle())

        for index in range(10):
            q_rand = Quaternion.random()
            q1 = q1 + q_rand
            q2 = q2 + pyQuaternion(q_rand.get_turtle())

        [self.assertLess(abs(q1[index]) - abs(q2[index]), 1e-8) for index in range(4)]

    def test_add_2(self):
        q1 = Quaternion.random()
        q2 = pyQuaternion(q1.get_turtle())

        for index in range(10):
            q_rand = Quaternion.random()
            q1 += q_rand
            q2 += pyQuaternion(q_rand.get_turtle())

        [self.assertLess(abs(q1[index]) - abs(q2[index]), 1e-8) for index in range(4)]

    def test_sub_1(self):
        q1 = Quaternion.random()
        q2 = pyQuaternion(q1.get_turtle())

        for index in range(10):
            q_rand = Quaternion.random()
            q1 = q1 - q_rand
            q2 = q2 - pyQuaternion(q_rand.get_turtle())

        [self.assertLess(abs(q1[index]) - abs(q2[index]), 1e-8) for index in range(4)]

    def test_sub_2(self):
        q1 = Quaternion.random()
        q2 = pyQuaternion(q1.get_turtle())

        for index in range(10):
            q_rand = Quaternion.random()
            q1 -= q_rand
            q2 -= pyQuaternion(q_rand.get_turtle())

        [self.assertLess(abs(q1[index]) - abs(q2[index]), 1e-8) for index in range(4)]

    def test_mul_1(self):
        q1 = Quaternion.random()
        q2 = pyQuaternion(q1.get_turtle())

        for index in range(3):
            q_rand = Quaternion.random()
            q1 = q1 * q_rand
            q2 = q2 * pyQuaternion(q_rand.get_turtle())

        [self.assertLess(abs(q1[index]) - abs(q2[index]), 1e-3) for index in range(4)]

    def test_mul_2(self):
        q1 = Quaternion.random()
        q2 = pyQuaternion(q1.get_turtle())

        for index in range(3):
            q_rand = Quaternion.random()
            q1 *= q_rand
            q2 *= pyQuaternion(q_rand.get_turtle())

        [self.assertLess(abs(q1[index]) - abs(q2[index]), 1e-3) for index in range(4)]

    def test_truediv_1(self):
        q1 = Quaternion.random()
        q2 = pyQuaternion(q1.get_turtle())

        for index in range(10):
            q_rand = Quaternion.random()
            q1 = q1 / q_rand
            q2 = q2 / pyQuaternion(q_rand.get_turtle())

        [self.assertLess(abs(q1[index]) - abs(q2[index]), 1e-8) for index in range(4)]

    def test_truediv_2(self):
        q1 = Quaternion.random()
        q2 = pyQuaternion(q1.get_turtle())

        for index in range(10):
            q_rand = Quaternion.random()
            q1 /= q_rand
            q2 /= pyQuaternion(q_rand.get_turtle())

        [self.assertLess(abs(q1[index]) - abs(q2[index]), 1e-8) for index in range(4)]

    def test_conjugate(self):
        q = Quaternion.random()
        q1 = q.conjugate()
        q2 = pyQuaternion(q.get_turtle()).conjugate

        [self.assertLess(abs(q1[index]) - abs(q2[index]), 1e-8) for index in range(4)]

    def test_norm(self):
        q = Quaternion.random()
        self.assertLess(pyQuaternion(q.get_turtle()).norm - q.norm(), 1e-8)

    def test_neg(self):
        q = Quaternion.random()
        q1 = -q
        q2 = -pyQuaternion(q.get_turtle())

        [self.assertLess(abs(q1[index]) - abs(q2[index]), 1e-8) for index in range(4)]


if __name__ == '__main__':
    unittest.main()
