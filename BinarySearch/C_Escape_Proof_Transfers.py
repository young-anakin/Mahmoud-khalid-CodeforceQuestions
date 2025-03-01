n, t, c = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
a = 0
b = c
# fl = True
cp = 0
ans = 0
for i in range(c):
    if arr[i] > t:
        cp +=1
        # fl = False

if cp == 0:
    ans += 1

while b < n:
    if arr[a] > t:
        cp -=1
    if arr[b] > t:
        cp +=1
    
    if cp == 0:
        ans +=1
    
    a +=1
    b +=1

print(ans)


