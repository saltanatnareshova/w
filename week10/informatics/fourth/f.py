n = int(input())
s = input().split(' ')
count=0
for i in range(0,n-2):
    if int(s[i+1])>int(s[i]) and  int(s[i+1])>int(s[i+2]):
        count =count+1
print(count)
