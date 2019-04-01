a=[]
n = int(input())
k=0
for i in range(n):
    new = int(input())
    a.append(new)
for i in range(n):
    k = k+a[i]
print(k)
