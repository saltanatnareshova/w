import math
n = int(input())
for i in range(n):
    if math.pow(2,i)<=n:
        print(int(math.pow(2,i)))
