t = int(input())
import bisect
for _ in range(t):
    n, q = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    arr.sort(reverse=True)
    ps = [0]
    for ind in range(len(arr)):
        ps.append(arr[ind] + ps[-1])
    # print(ps)
    for _ in range(q):
        val = int(input())
        x = bisect.bisect_left(ps, val)
        if x >= len(ps):
            print(-1)
        else:
            print(x)