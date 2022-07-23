f = open("27A.txt")
n = int(f.readline())
ms = 0
a = [int(x) for x in f]
for i in range(n):
    s = 0
    for j in range(i,n):
        s +=a[j]
        if s%28 == 0:
            ms = max(ms,s)
print(ms)

