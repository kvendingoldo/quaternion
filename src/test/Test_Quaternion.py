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
        q1 = Quaternion((1, 2, 3, 4))
        q2 = Quaternion((-2, 0, 1, 18))

        q3 = pyQuaternion(q1.get_turtle()) + pyQuaternion(q2.get_turtle())
        q4 = q1 + q2

        [self.assertEqual(q3[index], q4[index]) for index in range(4)]

    def test_add_2(self):
        q1 = Quaternion.rand()
        q2 = Quaternion.rand()

        q3 = pyQuaternion(q1.get_turtle()) + pyQuaternion(q2.get_turtle())
        q4 = q1 + q2

        [self.assertEqual(q3[index], q4[index]) for index in range(4)]

    def test_sub_2(self):
        q1 = Quaternion.rand()
        q2 = Quaternion.rand()

        q3 = pyQuaternion(q1.get_turtle()) - pyQuaternion(q2.get_turtle())
        q4 = q1 - q2

        [self.assertEqual(q3[index], q4[index]) for index in range(4)]

    def test_sub_3(self):
        q1 = Quaternion((0, 0, 0, 0))
        q2 = Quaternion.rand(10000)

        q3 = pyQuaternion(q1.get_turtle()) - pyQuaternion(q2.get_turtle())
        q4 = q1 - q2

        [self.assertEqual(q3[index], q4[index]) for index in range(4)]

    def test_mul_1(self):
        q1 = Quaternion.rand()
        q2 = Quaternion.rand()

        q3 = pyQuaternion(q1.get_turtle()) * pyQuaternion(q2.get_turtle())
        q4 = q1 * q2

        [self.assertLess(q3[index]-q4[index], 1e-8) for index in range(4)]

    def test_mul_2(self):
        q1 = Quaternion.rand()
        q2 = Quaternion((0, 0, 0, 0))

        q3 = pyQuaternion(q1.get_turtle()) * pyQuaternion(q2.get_turtle())
        q4 = q1 * q2

        [self.assertLess(q3[index]-q4[index], 1e-8) for index in range(4)]

    def test_mul_3(self):
        q1 = Quaternion.rand()
        q2 = Quaternion((5, 0, 0, 0))

        q3 = pyQuaternion(q1.get_turtle()) * pyQuaternion(q2.get_turtle())
        q4 = q1 * q2

        [self.assertLess(q3[index]-q4[index], 1e-8) for index in range(4)]

    def test_mul_4(self):
        q1 = Quaternion.rand()
        q2 = Quaternion((0, 1, 3, 4))

        q3 = pyQuaternion(q1.get_turtle()) * pyQuaternion(q2.get_turtle())
        q4 = q1 * q2

        [self.assertLess(q3[index]-q4[index], 1e-8) for index in range(4)]

    def test_truediv_1(self):
        q1 = Quaternion.rand()
        q2 = Quaternion.rand()

        q3 = pyQuaternion(q1.get_turtle()) / pyQuaternion(q2.get_turtle())
        q4 = q1 / q2

        [self.assertLess(q3[index]-q4[index], 1e-8) for index in range(4)]

    def test_norm(self):
        q = Quaternion.rand()
        self.assertLess(pyQuaternion(q.get_turtle()).norm - q.norm(), 1e-8)

    @unittest.skip("troubles...")
    def test_neg(self):
        q = Quaternion.rand()

        q1 = -q
        q2 = -pyQuaternion(q.get_turtle())

        [self.assertEqual(q1[index], q2[index]) for index in range(4)]





if __name__ == '__main__':
    unittest.main()
