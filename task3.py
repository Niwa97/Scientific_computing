#1
def my_print(x):
  for i in range(x):
    print("+---", end='')
  print("+")

st = "Mariusz"
my_print(len(st))
for i in range(len(st)):
  print("|", st[i], "", end='')
print("|")
my_print(len(st))

#2
for i in range(1,41):
  if(i%5 ==0 and i%7 == 0):
    print("x is divided by 5 and 7 -", i )
  elif(i%5 ==0):
    print("x is divided by 5 -", i) 
  elif(i%7 == 0):
    print("x is divided by 7 -", i)
  elif(i != 13):
    print("x is not important -", i)

j = 1
while(j < 41):
  if(j%5 == 0 and j%7 == 0):
    print("x is divided by 5 and 7 -", j)
  elif(j%5 ==0):
    print("x is divided by 5 -", j) 
  elif(j%7 == 0):
    print("x is divided by 7 -", j)
  elif(j != 13):
    print("x is not important -", j)
  j = j + 1
  
#3
import math
n = 2022
x = math.pi
word = "Python"
english = "book"
x = "{:.5f}".format(x)
f = open("vars.txt", "w")
f.write(str(n)+ '\n')
f.write(str(x)+ '\n')
f.write(word+ '\n')
f.write(english)
f.close()
with open('vars.txt', 'r') as f2:
    print(f2.read())
