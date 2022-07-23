f = open("27B.txt")
n = int(f.readline())
m = [10**30]*28
ms = 0
s = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if s%28 == 0: ms = s
    ms = max(ms,s-m[s%28])
    m[s%28] = min(m[s%28],s)
print(ms)

