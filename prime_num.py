# prime not prime

number = int(input("Enter the number: "))
f = 0
for i in range(2, int(number/2)):
    if (number % i) == 0:
        print(f"{number} is divisible by {i}, so not prime!")
        f = 1
        break

if (f == 0):
    print('prime!')
