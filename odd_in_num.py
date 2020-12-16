# Write a program to print odd numbers available in a enters number?

number = 1234
print(f"the odd digits in {number} are", end=" ")
while(number > 0):
    a = number % 10
    if (a % 2) != 0:
        print(a, end=",")

    number = int(number/10)
