"""
WAP to read a string and display the longest
substring of the given string having just the constant.
"""
s = "WAP to read a string and display the longest substring of the given string having just the constant"

s1 = s.split(' ')
# s1.sort()
n = len(s1)
# temp = ''
for i in range(n-1):
    for j in range(0, n - i-1):
        if len(s1[j]) > len(s1[j+1]):
            s1[j], s1[j+1] = s1[j+1], s1[j]

print(f"'{s1[-1]}' is the longest string")
