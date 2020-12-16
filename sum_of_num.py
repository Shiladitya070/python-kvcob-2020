# Write a python program to print the sum of all the digit of a number?

number = int(input("Enter the Number: "))
_sum = 0
while(number > 0):
    last = number % 10 
    _sum = last + _sum
    number = int(number/10)

print(_sum)