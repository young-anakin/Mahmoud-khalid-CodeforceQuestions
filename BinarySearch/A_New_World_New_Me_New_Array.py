n, x = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
both = []
import bisect
valid = False
arr2 = list(sorted(arr))
first, second = 0, 0
for i in range(len(arr)):
    mn = bisect.bisect_left(arr, x-arr2[i])
    if mn < len(arr2):
        if arr2[mn] + arr2[i] == x:
            if mn == i:
                if arr2.count(arr2[mn]) > 1:
                    xx = []
                    for i in range(len(arr)):
                        if arr[i] == arr2[mn]:
                            xx.append(i)
                    print(xx[0]+1, xx[1]+1)
                    exit()
                else:
                    continue
            first, second = arr2[i], arr2[mn]
            valid = True
            break


if not valid:
    print(-1)
else:
    a, b = arr.index(first), arr.index(second)
    print(a+1, b+1)
    