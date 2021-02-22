# insertiion sort

L = [2, 54, 6, 7, 10, 3, 46]

for i in range(len(L)):
    k = L[i]
    j = i - 1
    while j > 0 and k < L[j]:
        L[j+1] = L[j]
        j = j - 1
    else:
        L[j+1] = k

print(L)
