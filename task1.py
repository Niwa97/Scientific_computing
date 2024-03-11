#1.1
a = 1000010010
s = str(a)
num_of_zeros = 0
for i in range(len(s)):
  if(s[i]=="0"):
    num_of_zeros = num_of_zeros + 1

print(num_of_zeros)

#1.2
x = 5
print(x == 5 and 3 + 8)  # 11 - x==5 is true and second operation 3+8 is being executed
print(x == 4 and 3 + 8)  # False - x==4 is false then conjunction is false - second condition is not checked
print(3 + 8 and x == 5)  # True - any non-zero numeric type is considered true nd second operation is being executed
print(3 + 8 and x == 4)  # False - The same here but the second operation returns false

print(isinstance(True, int))   # True - True is instance of int from historic reasons (bool is subclass of int and previoursly 0 and 1 were truth and false values)
print(isinstance(True, bool))  # True - True is instance of bool in newest wersions of python

#1.3
odd = [x for x in range(101) if x%2==1]
s = sum(odd)
print(s)

#1.4a
name = "Mariusz"
name_chars = [*name]
name_unicode = []
for i in range(len(name_chars)):
  name_unicode.append(ord(name_chars[i]))
print(name_unicode)

#1.4b
pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), (3,"Lithium","Li",7), (4,"Berylium","Be",9), (5,"Boron","Bo",11), (6,"Carbon","C",12), (7,"Nitrogen","N",14), (8,"Oxygen","O",16), (9,"Fluorine","F",19), (10,"Neon","Ne",20)]
h = ['Atomic number', 'Name', 'Symbol', 'Mass']
print('| {:<14s} | {:<9s} | {:<7s} | {:<5} |'.format(*h))
for (n, name, symbol, weight) in pt:
  print('| {:<14} | {:<9} | {:<7} | {:<5} |'.format(*(n, name, symbol, weight)))

#1.5
iliad = "Gniew, Bogini, opiewaj Achilla, syna Peleusa, zgubę niosący i klęski nieprzeliczone Achajom, co do Hadesu tak wiele dusz bohaterów potężnych strącił, a ciała ich wydał na pastwę sępom drapieżnym oraz psom głodnym. Tak Dzeusa dokonywała się wola. Zwłaszcza od dnia, gdy w niezgodzie przeciwko sobie stanęli władca narodów Atryda i bogom równy Achilles."
iliad = iliad.replace(",", "")
iliad = iliad.replace('.', "")
iliad = iliad.lower()
black_char_count = 0
for i in iliad:
  if i != " ":
    black_char_count = black_char_count + 1;
print(black_char_count)
words = iliad.split(" ")
longest_word = words[0]
for i in words:
  if len(longest_word) < len(i):
    longest_word = i
print(longest_word)
print(sorted(words))
words.sort(key = len)
print(words)

#1.6
t = (2, 4)
print(t[1]) #2 is out of scope indexing begins at 0
t_append = t + (6,) #tuple is not a list - no append method
a, b = t; #unpacking tuple - assigning first value to a and second to b
print(a, b)

#1.7
dict1 = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
list1 = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
list2 = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
dict2 = {list1[i]: list2[i] for i in range(len(list1))}
dict3 = dict((list1[i], list2[i]) for i in range(len(list1)))
