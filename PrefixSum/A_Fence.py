n, t = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

i, j = 0, t
mx = float("inf")
ans = -1
cp = 0
for ind in range(j):
    cp += arr[ind]

ans = 0
mx = cp
# print(mx)
while j < n:
    cp -= arr[i]
    cp += arr[j]

    i +=1
    j +=1
    # print(mx)
    if cp < mx:
        mx = cp
        ans = i

print(ans+1)

    