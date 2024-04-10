import math
import unittest

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
      return "Vector("+self.x+self.y+self.z+")"

    def __eq__(self, other):
      if(self.x == other.x and self.y == other.y and self.z == other.z):
        return True
      else:
        return False

    def __ne__(self, other):       
      return not self == other

    def __add__(self, other):
      return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
      return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
      return (self.x * other.x + self.y * other.y + self.z * other.z)

    def cross(self, other):
      return Vector(self.y*other.z - other.y*self.z, self.z*other.x - other.z*self.x, self.x*other.y - other.x*self.y)

    def length(self):
      return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def scale(self, alpha):
      return Vector(alpha*self.x, alpha*self.y, alpha*self.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

def test_constructor():
    v = Vector(3, 2, 1)
    assert type(v) == Vector
    assert v.x == 3
    assert v.y == 2
    assert v.z == 1

def test_addition():
    v1 = Vector(1,1,1)
    v2 = Vector(2,2,2)
    v3 = v1 + v2
    assert v3.x == 3
    assert v3.y == 3
    assert v3.z == 3

def test_subtraction():
    v1 = Vector(2,2,2)
    v2 = Vector(1,1,1)
    v3 = v1 - v2
    assert v3.x == 1
    assert v3.y == 1
    assert v3.z == 1

def test_scaling():
    v1 = Vector(1,1,1)
    a = 3
    v2 = v1.scale(3)
    assert v2.x == 3
    assert v2.y == 3
    assert v2.z == 3

def test_equality():
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 == v2

def test_multiplication():
    v1 = Vector(1,1,1)
    v2 = Vector(1,1,0)
    a = v1*v2
    assert a == 2

def test_cross():
    v1 = Vector(1,0,0)
    v2 = Vector(0,1,0)
    v3 = v1.cross(v2)
    v4 = Vector(0,0,1)
    assert v3 == v4

def test_norm():
    v1 = Vector(12,5,0)
    assert 13 == v1.length()

test_constructor()
test_addition()
test_subtraction()
test_scaling()
test_equality()
test_multiplication()
test_cross()
test_norm()
