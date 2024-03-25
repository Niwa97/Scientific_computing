#1
p=(1/2,1/2)
x = lambda a : (a[0]**2 + a[1]**2) <= 1
y = lambda a : (a[0] > 0 and a[1] > 0)
print(x(p))
print(y(p))
L1 = [(0,0), (1/2,1/2), (1/3, 1/2), (5/8, 1/2), (1,0), (0,1), (1,1)]
L1.sort(key=lambda a: (-a[1], a[0]) )
print(L1)
L2 = [(1,1), (0,0), (5/8, 1/2), (1/2,-1/2)]
L2.sort(key=lambda a: abs(a[0]) + abs(a[1]) )
print(L2)

#2
def reverse_range(L, left, right):
  L[left:right+1] = L[left:right+1][::-1]
  return L

def reverse_range_iter(L, left, right):
  for i in range(left, int((left + right)/2)+1):
    temp = L[i]
    L[i] = L[right + left -i]
    L[right + left -i] = temp
  return L
  
def reverse_range_rec(L, left, right):
  if(left < right):
    temp = L[left]
    L[left] = L[right]
    L[right] = temp
    left = left + 1
    right = right - 1
    reverse_range_rec(L, left, right)
  return L
  
L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(id(L1))
reverse_range(L1, 3, 7)
print(id(L1))
print(L1)
print(id(L2))
reverse_range_iter(L2, 3, 7)
print(id(L2))
print(L2)
print(id(L3))
reverse_range_rec(L3, 3, 7)
print(id(L3))
print(L3)

#3
def even():
  i = 0
  while True:
    yield i
    i = i + 2

def odd():
  i = 1
  while True:
    yield i
    i = i + 2

def squares(k):
  i = 0
  while True:
    yield k**i
    i = i + 1
