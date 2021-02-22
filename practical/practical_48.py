"""
WAP to calculate the value of the following Taylor
series-
Y=x 1 /1! + x 2 /2! + x 3 /3! +x 4 /4! + x 5 /5! + ……+n
Where, n will be entered by the user.
"""

import math

n = int(input("Enter N:"))

x = 2
e_to_2 = 0
for i in range(n):
    e_to_2 += x**i/math.factorial(i)
    print(e_to_2)

print(e_to_2)
