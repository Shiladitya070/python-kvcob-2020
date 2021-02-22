"""
Compute the greatest common divisor and the least
common multiple of two integers.
"""

a = int(input("Enter small number:"))
b = int(input("Enter bigger number:"))

gcd = 1

if (b % a == 0):
    gcd = a
else:
    print("b//2:", int(b//2))
    for i in range(int(b//2), 1, -1):
        print(i)
        if (b % i == 0 and a % i == 0):
            gcd = i
            break

lcm = (a*b)/gcd

print(f"gcd:{gcd} || lcm:{lcm}")
