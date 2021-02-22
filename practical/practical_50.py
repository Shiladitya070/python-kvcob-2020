"""

WAP to generate a random number between 1 to 100
and print “You Won” if the number is predefined
lucky number.

"""

import random

lucky_numbers = [1, 40, 50, 87, 77, 99, 69, 57]

for i in range(3):
    drawn_number = random.randint(1, 100)
    print("You got number:", drawn_number)

    if drawn_number in lucky_numbers:
        print("you won")
        break
    else:
        input("try again")
