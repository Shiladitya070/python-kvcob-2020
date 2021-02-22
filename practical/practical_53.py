"""
WAP to read a string and print total number of
vowels and consonant available in the string.
"""

s = "WAP to read a string and print total number of vowels and consonant available in the string."
V_count = 0
c_const = 0
for i in s:
    if (i.lower() in "aeiou"):
        V_count += 1
    else:
        c_const += 1
print(f"vowels = {V_count} || constant = {c_const}")
