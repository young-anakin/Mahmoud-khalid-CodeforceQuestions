n = int(input())
arr = list(map(int, input().split(" ")))

import bisect

arr.sort()
mx = -1

# print(arr)

for ind in range(len(arr)):
    x = arr[ind] + 5
    ans = bisect.bisect_right(arr, x, ind)
    mx = max(mx, abs(ind - ans))

print(mx)