n = int(input("Enter the number: "))
while(n > 0):
    a = n % 10
    print(a, end="")
    n = int(n/10)
