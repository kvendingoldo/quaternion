from math import sqrt


class Quaternion(object):
    def __init__(self, real=0.0, im_i=0.0, im_j=0.0, im_k=0.0):
        self.real = real
        self.im_i = im_i
        self.im_j = im_j
        self.im_k = im_k

    def __init__(self, obj):
        if isinstance(obj, Quaternion):
            self = obj
        elif isinstance(obj, (int, long, float)):
            self.real = obj
            self.im_i = 0.0
            self.im_j = 0.0
            self.im_k = 0.0
        elif isinstance(obj, (list, tuple)):
            if len(obj) == 4:
                self.real = obj[0]
                self.im_i = obj[1]
                self.im_j = obj[2]
                self.im_k = obj[3]
            else:
                raise ValueError('Len is less than 4')
        else:
            raise ValueError('')

    def __add__(self, other):
        return Quaternion(
            self.real + other.real,
            self.im_i + other.im_i,
            self.im_j + other.im_j,
            self.im_k + other.im_k
        )

    def __iadd__(self, other):
        self = self.__add__(other)

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
        self = self.__sub__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        '''
        (a + i b + j c + k d) * (e + i f + j g + k h) =
        a*e - b*f - c*g- d*h +
        i (b*e + a*f + c*h - d*g) +
        j (a*g - b*h + c*e + d*f) +
        k (a*h + b*g - c*f + d*e)
        '''
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
        elif isinstance(other, (int, long, float)):
            return Quaternion(
                other * self.real,
                other * self.im_i,
                other * self.im_j,
                other * self.im_k
            )
        else:
            raise ValueError(other + ' value is incorrect')

    def __imul__(self, other):
        self = self.__mul__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def norm(self):
        """ L2 norm of the Quaternion 4-vector. """
        return self.real**2 + self.im_i**2 + self.im_j**2 + self.im_k**2

    def __abs__(self):
        return sqrt(self.norm())

    def vector_mul(self, other):
        other = Quaternion(other)
        return self * other

    def __neg__(self):
        return Quaternion(self.real, -self.im_i, -self.im_j, -self.im_k)

    def __eq__(self, other):
        return self.real == other.real and self.im_i == other.im_i and \
                self.im_j == other.im_j and self.im_k == other.im_k

    def __ne__(self, other):
        return not self.__eq__(other)

    def __div__(self, other):
        other = Quaternion(other)
        return self * (-other) / (abs(other) ** 2)

    def __idiv__(self, other):
        self = self.__div__(other)

    def __rdiv__(self, other):
        return self.__div__(other)

    def __str__(self):
        return '(%g, %g, %g, %g)' % (self.real, self.im_i, self.im_j, self.im_k)

    def __repr__(self):
        return 'q = %g*1 + %g*i + %g*j + %g*k' % (self.real, self.im_i,
                                                  self.im_j, self.im_k)

    def random(self, range_of_val):
        return Quaternion(
            uniform(randrange(range_of_val), randrange(range_of_val)),
            uniform(randrange(range_of_val), randrange(range_of_val)),
            uniform(randrange(range_of_val), randrange(range_of_val)),
            uniform(randrange(range_of_val), randrange(range_of_val)),
        )

    def random(self):
        return Quaternion(
            uniform(randrange(1000), randrange(1000)),
            uniform(randrange(1000), randrange(1000)),
            uniform(randrange(1000), randrange(1000)),
            uniform(randrange(1000), randrange(1000)),
        )

    def unit(self):
        self.__init__(0, 1, 0, 0)

    def scalar():
        """ Return the real or scalar component of the Quaternion object. """
        return self.real

    def vector():
        """ array of the 3 imaginary elements of the Quaternion object. """
        return [self.im_i, self.im_j, self.im_k]

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

    def __invert__(self):
        # wtf?
        return (self == Quaternion(0.0))

# add trigonometric form + unittests

quaternion = Quaternion()
print abs(quaternion)
