n, x = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

import bisect

for i in arr:
    rem = bisect.bisect_left(arr, (x-i))
    print