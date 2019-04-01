a=[]
n = int(input())
count=0
for i in range(n):
    new = int(input())
    a.append(new)
for i in range(n):
    if a[i]==0:
        count=count+1
print(count)
