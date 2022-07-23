f = open("27B.txt")
n = int(f.readline())
s = []
ans = []
for i in range(n):
    x = int(f.readline())
    s = [a+x for a in s] + [x]
    s = {a%28:a for a in sorted(s)}
    if 0 in s: ans.append(s[0])
    s = s.values()
print(max(ans))






    
    
