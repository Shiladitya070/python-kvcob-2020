'''
Exercire 1:
WAP to read an length and width of a rectangle and print area & perimeter
WAP to read radius of a circle and print it's area & circumfercene
convent celcius and farahite
'''
# ----Area and perimeter of a rectangle----
print('----Area and perimeter of a rectangle----')

length = int(input('Enter the length of the Rectangle: '))
width = int(input('Enter the width of the Rectangle: '))

print(f'Area of the rectangle is {length * width}')
print(f'Perimeter of of the reactangle is { 2*(length + width) }')
print()
# ----Area and perimeter of a rectangle----

# ----Area and circumference of a circle----
print('----Area and circumference of a circle----')

radius = int(input('Enter the radius of the circle: '))

print(f'Area of the circle is {3.14 * radius**2}')
print(f'Circumeference of the circle is {2 * 3.14 * radius}')
print()
# ----Area and circumference of a circle----


print('----celcius to fahrenheit----')

celcius = int(input('Enter the tempareture in celcius: '))

fahrenheit = (celcius * (9/5)) + 32

print(f'fahrenheit of {celcius}॰c is {fahrenheit}॰f')
