# x = 1/1! + 2/2! + 3/3! + 4/4! + ... n/n!
import math

n = int(input("enter the number:"))
x = 0
for i in range(1, n+1):
    x = x + (i+2/math.factorial(i))
print(x)
