n, t = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
import bisect
ps = [0]
for i in arr1:
    ps.append(ps[-1] + i)

arr = list(map(int, input().split(" ")))
for i in arr:
    z = bisect.bisect_left(ps, i)
    print(z, i- ps[z-1])

# print(ps)