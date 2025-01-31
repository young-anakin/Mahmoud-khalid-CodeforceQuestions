n, m = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
ps = [0 for _ in range(n)]
for _ in range(m):
    u, v = list(map(int, input().split(" ")))
    ps[u-1] +=1
    if v == n:
        continue
    else:
        ps[v] -=1

# print(ps)
for ind in range(1, n):
    ps[ind] = ps[ind] + ps[ind-1]
ps.sort(reverse=True)
arr.sort(reverse=True)
cp = 0
for ind in range(len(arr)):
    cp += ps[ind] * arr[ind]
print(cp)