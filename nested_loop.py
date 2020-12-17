# nested loop date-17 dec 2020
"""
a = 1

while (a < 3):
    b = 10 # <---
    while (b > 7):
        print(a, b)
        b = b - 1
    a = a + 1

output: 
1 10
1 9 
1 8 
2 10
2 9 
2 8 
"""
"""
a = 1
b = 10  # <---
while (a < 3):
    while (b > 7):
        print(a, b)
        b = b - 1
    a = a + 1

output: 
1 10
1 9
1 8
"""

"""
for a in range(1, 3):
    for b in range(10, 7, -1):
        print(a, b)

output:
1 10
1 9
1 8
2 10
2 9
2 8
"""
# WAP to print all prime in a given range a and b?
'''
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))

for n in range(num1, num2):
    f = 0
    for i in range(2, n//2):
        if (n % i == 0):
            f = 1
            break
    if(f == 0):
        print('Prime:', n)
'''
'''
Q.print this using loops
    a)  12345
        12345
        12345
        12345
    b)  *****
        *****
        *****
        *****
for i in range(4):
    for e in range(1, 6):
        print(e, end="")
    print()
for i in range(4):
    for e in range(1, 6):
        print("*", end="")
    print()
'''
'''
#  print the pattern:
#     12345
#     1234
#     123
#     12
#     1

for r in range(6, 1, -1):
    for c in range(1, r):
        print(c, end="")
    print()
'''
'''
HW: print the pattern:
    ***** *****
    ****   ****
    ***     ***
    **       **
    *         *
'''