n = int(input())
s = input().split(' ')
count=0
for i in range(1,n):
    if int(s[i])>int(s[i-1]):
        count+=1
print(count)
