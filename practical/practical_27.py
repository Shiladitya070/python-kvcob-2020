"""
Write a program to print following pattern on screen-
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""

for r in range(6):
    # print(r)
    for c in range(r+1):
        print("*", end=" ")
    print()

for r in range(5, 0, -1):
    # print(r)
    for c in range(r, 0, -1):
        print("*", end=" ")
    print()
