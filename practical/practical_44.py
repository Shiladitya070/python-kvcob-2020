"""
Write a Python Program to input some numbers in a
tuples and create second tuple which contain only
unique values (non-repeating) values from the first
tuple.
"""

L = []
Uni_L = []
Dupli_L = []

l_size = int(input("enter the size:"))

for i in range(l_size):
    ele = int(input("enter the element:"))
    L.append(ele)
L.sort()
print(L)

for i in L:
    freq = L.count(i)
    if freq == 1:
        Uni_L.append(i)
    else:
        if i not in Dupli_L:
            Dupli_L.append(i)

T_UNi = tuple(Uni_L)
T_Dupli = tuple(Dupli_L)
print("Unique elements:", T_UNi)
print("Duplicate elements:", T_Dupli)
