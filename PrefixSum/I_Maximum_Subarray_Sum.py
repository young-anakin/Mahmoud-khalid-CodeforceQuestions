
t = int(input())
from collections import defaultdict
for _ in range(t):
    dd = defaultdict(int)
    n = int(input())
    arr = list(map(int, input().split(" ")))
    ps = [0]
    for ind in arr:
        ps.append(ps[-1] + ind)
    
    yasir = sum(arr)
    mx = -1 * float('inf')
    mn = 0
    # print(ps)
    for ind in range(len(ps)):
        ind = ps[ind]
        # print(ind - mn)
        dd[ind - mn] +=1
        mx = max(mx, ind - mn)
        mn = min(mn, ind)
    
    # if mx < yasir:
    #     print("YES")
    # else:
    #     print("NO")
    # print(ps)
    if dd[0] == 1:
        del dd[0]

    mx = max(dd)
    if mx > yasir:
        print("NO")
    elif mx == yasir:
        if dd[mx] > 1:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
    # print(mx, dd[mx])
    # print(dd)
    # print(ps, yasir)
    # print(mx)