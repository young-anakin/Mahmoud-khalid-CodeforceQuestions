t = int(input())
import bisect
arr = list(map(int, input().split(" ")))
n = int(input())
arr.sort()
for _ in range(n):
    x = int(input())
    ans = bisect.bisect_right(arr, x)
    print(ans)