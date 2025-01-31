n = int(input())
import bisect
arr = list(map(int, input().split(" ")))
ps = [0]
for ind in range(len(arr)):
    ps.append(ps[-1] + arr[ind])

t = int(input())
x = list(map(int, input().split(" ")))
for ind in range(t):
    ans = bisect.bisect_left(ps, x[ind])
    print(ans)