import itertools
import random
import math

#1

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
      return "Vector("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

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
    
    def iszero(self):
      if(self.x == 0 and self.y == 0 and self.z == 0):
        return True
      else:
        return False

    def __hash__(self):
        return hash((self.x, self.y, self.z))

class CrossProductException(Exception):
  def __init__(self, message="Vectors do not span the plane"):
        self.message = message
        super().__init__(self.message)

def find_axis(v1, v2):
  if(v1.iszero() == True or v2.iszero() == True or v1.cross(v2).iszero() == True ):
      raise CrossProductException #ValueError also can be raised here
  else:
      return v1.cross(v2)
  
v1 = Vector(1,0,0)
v2 = Vector(0,1,0)
print(find_axis(v1,v2))

#2

class BinaryIterator:
  def __init__(self):
    self.n = 0

  def __iter__(self):
    return self

  def __next__(self):
    x = self.n
    self.n = (self.n + 1)%2
    return x

class OscilatingBinIterator:
  def __init__(self):
    self.n = 0
    self.flag = 0

  def __iter__(self):
    return self

  def __next__(self):
    x = self.n
    if(self.flag == 0):
      self.n = (self.n + 1)%2
      if(self.n == 1):
        self.flag = 1
    elif(self.flag == 1):
      self.n = -((self.n + 1)%2)
      if(self.n == -1):
        self.flag = 0
    else:
      raise ValueError
    return x

class RandomIterator:
  def __init__(self):
    self.n = 0

  def __iter__(self):
    return self

  def __next__(self):
    x = self.n
    random.seed()
    self.n = random.randint(0,1)
    return x

biniter = BinaryIterator()
osciter = OscilatingBinIterator()
randiter = RandomIterator()

print("a) iteration")
for _ in range(15):
  print(next(biniter))

print("b) iteration")
for _ in range(15):
  print(next(randiter))

print("c) iteration")
for _ in range(15):
  print(next(osciter))
