n, m = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
ps = [0]
from collections import Counter
ss = set()

cp = Counter(arr)
tot = len(cp)
ps[0] = len(cp)
# print(cp)
for ind in arr:
    cp[ind] -=1
    if cp[ind] == 0:
        del cp[ind]
    ps.append(len(cp))

# ps = ps[1:]

    # else:
    #     ps.append(ps[-1])
# print(ps)
for _ in range(m):
    val = int(input())
    print(ps[val-1])