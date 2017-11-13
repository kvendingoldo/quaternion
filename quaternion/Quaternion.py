# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import numpy as np


class Quaternion(object):
    def __init__(self, *args):
        tmp = [arg for arg in args]
        items = tmp[:4] + [0] * (4 - len(tmp))
        self.real = items[0]
        self.im_i = items[1]
        self.im_j = items[2]
        self.im_k = items[3]
        if len(args) > 4:
            raise ValueError('Was passed more 5 elements to constructor')

    def __add__(self, other):
        return Quaternion(
            self.real + other.real,
            self.im_i + other.im_i,
            self.im_j + other.im_j,
            self.im_k + other.im_k
        )

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Quaternion(
            self.real - other.real,
            self.im_i - other.im_i,
            self.im_j - other.im_j,
            self.im_k - other.im_k
        )

    def __isub__(self, other):
        return self.__sub__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        """
        (a + i b + j c + k d) * (e + i f + j g + k h) =
        a*e - b*f - c*g- d*h +
        i (b*e + a*f + c*h - d*g) +
        j (a*g - b*h + c*e + d*f) +
        k (a*h + b*g - c*f + d*e)
        """
        if isinstance(other, Quaternion):
            return Quaternion(
                self.real * other.real - self.im_i * other.im_i -
                self.im_j * other.im_j - self.im_k * other.im_k,

                self.im_i * other.real + self.real * other.im_i +
                self.im_j * other.im_k - self.im_k * other.im_j,

                self.real * other.im_j - self.im_i * other.im_k +
                self.im_j * other.real + self.im_k * other.im_i,

                self.real * other.im_k + self.im_i * other.im_j -
                self.im_j * other.im_i + self.im_k * other.real
            )
        elif isinstance(other, (int, float)):
            return Quaternion(
                other * self.real,
                other * self.im_i,
                other * self.im_j,
                other * self.im_k
            )
        else:
            raise ValueError(other + ' value is incorrect')

    def __imul__(self, other):
        return self.__mul__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __abs__(self):
        return np.sqrt(self.norm)

    def __neg__(self):
        return Quaternion(self.real, -self.im_i, -self.im_j, -self.im_k)

    def __eq__(self, other):
        return self.real == other.real and self.im_i == other.im_i and \
               self.im_j == other.im_j and self.im_k == other.im_k

    def __ne__(self, other):
        return not self.__eq__(other)

    def __floordiv__(self, other):
        return self * ((-other) * (1 / (abs(other) ** 2)))

    def __truediv__(self, other):
        return self * ((-other) * (1 / (np.abs(other) ** 2)))

    def __idiv__(self, other):
        return self.__div__(other)

    def __rdiv__(self, other):
        return self.__floordiv__(other)

    def __str__(self):
        return '(%g, %g, %g, %g)' % (self.real, self.im_i, self.im_j, self.im_k)

    def __repr__(self):
        return 'q = %g*1 + %g*i + %g*j + %g*k' % (self.real, self.im_i,
                                                  self.im_j, self.im_k)

    def __invert__(self):
        """conjugate quaternion"""
        return Quaternion(self.real, -self.im_i, -self.im_j, -self.im_k)

    def __getitem__(self, index):
        if index == 0:
            return self.real
        elif index == 1:
            return self.im_i
        elif index == 2:
            return self.im_j
        elif index == 3:
            return self.im_k

    def __setitem__(self, index, value):
        if index == 0:
            self.real = value
        elif index == 1:
            self.im_i = value
        elif index == 2:
            self.im_j = value
        elif index == 3:
            self.im_k = value

    def __pow__(self, exponent):
        λ, cos_v, ξ, sin_v = self.trigonometric_form
        acos = np.arccos(cos_v)
        asin = np.arcsin(sin_v)

        φ_1 = np.degrees(acos)
        φ_2 = np.degrees(asin)

        cos_angle_1 = φ_1 + 360 * exponent
        cos_angle_2 = -φ_1 + 360 * exponent

        sin_angle_1 = φ_2 + 360 * exponent
        sin_angle_2 = 180 - φ_2 + 360 * exponent

        if np.fabs(cos_angle_1 - sin_angle_1) <= 1e-5:
            α = cos_angle_1

        elif np.fabs(cos_angle_1 - sin_angle_2) <= 1e-5:
            α = cos_angle_1

        elif np.fabs(cos_angle_2 - sin_angle_1) <= 1e-5:
            α = cos_angle_2

        elif np.fabs(cos_angle_2 - sin_angle_2) <= 1e-5:
            α = cos_angle_2

        λ_n = λ ** exponent

        return Quaternion(λ_n * np.cos(α), λ_n * ξ[0] * np.sin(α), λ_n * ξ[1] * np.sin(α), λ_n * ξ[2] * np.sin(α))

    def __ipow__(self, other):
        return self ** other

    def __rpow__(self, other):
        return other ** float(self)

    @staticmethod
    def random(rng=1000):
        return Quaternion(
            np.random.uniform(np.random.randint(rng), np.random.randint(rng)),
            np.random.uniform(np.random.randint(rng), np.random.randint(rng)),
            np.random.uniform(np.random.randint(rng), np.random.randint(rng)),
            np.random.uniform(np.random.randint(rng), np.random.randint(rng))
        )

    @staticmethod
    def unit():
        return Quaternion(0, 1, 0, 0)

    @staticmethod
    def zero():
        return Quaternion(0, 0, 0, 0)

    def get_turtle(self):
        return tuple((self.real, self.im_i, self.im_j, self.im_k))

    def print_trigonometric_form(self):
        λ, cos_v, ξ, sin_v = self.trigonometric_form

        acos = np.arccos(cos_v)
        asin = np.arcsin(sin_v)

        φ_1 = np.degrees(acos)
        φ_2 = np.degrees(asin)

        sin_angle_1 = φ_2
        sin_angle_2 = 180 - φ_2

        if np.fabs(φ_1  - sin_angle_1) <= 1e-5:
            α = φ_1

        elif np.fabs(φ_1  - sin_angle_2) <= 1e-5:
            α = φ_1

        elif np.fabs(-φ_1 - sin_angle_1) <= 1e-5:
            α = -φ_1

        elif np.fabs(-φ_1 - sin_angle_2) <= 1e-5:
            α = -φ_1

        print('q = %g(cos(%g) + (%g, %g, %g) * sin(%g))' % (λ, α, ξ[0], ξ[1], ξ[2], α))

    @property
    def trigonometric_form(self):
        tmp = np.sqrt(self[1] ** 2 + self[2] ** 2 + self[3] ** 2)
        λ = self.tensor
        cos_v = self.scalar/λ
        sin_v = tmp/λ
        ξ = list(map(lambda x: x * λ * sin_v, self.vector/tmp))
        return λ, cos_v, ξ, sin_v

    @property
    def norm(self):
        """ L2 norm of the Quaternion 4-vector. """
        return self.real ** 2 + self.im_i ** 2 + self.im_j ** 2 + self.im_k ** 2

    @property
    def tensor(self):
        """https://books.google.ru/books?id=jgx4CwAAQBAJ&pg=PA40&lpg=PA40&dq=%D0%BA%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD%D1%8B+%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0+%D0%BC%D1%83%D0%B0%D0%B2%D1%80%D0%B0&source=bl&ots=Nyq3yn1SOj&sig=aOpToTt0hUQ7dpIdK5HQI-QPtLw&hl=en&sa=X&ved=0ahUKEwjbpazrlrzXAhWiQJoKHUu2A8EQ6AEIOjAD#v=onepage&q=%D0%BA%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD%D1%8B%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0%20%D0%BC%D1%83%D0%B0%D0%B2%D1%80%D0%B0&f=false"""
        return np.sqrt(self.norm)

    @property
    def scalar(self):
        """ Return the real or scalar component of the Quaternion object. """
        return self.real

    @property
    def vector(self):
        """ Array of the 3 imaginary elements of the Quaternion object. """
        return list([self.im_i, self.im_j, self.im_k])
