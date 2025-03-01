t = int(input())
from collections import defaultdict
for _ in range(t):
    n , k = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    og = []
    for i in range(n):
        og.append((arr[i], i))
    
    og.sort()
    b.sort()
    dd = defaultdict(int)
    # for i in range(len(arr)):
    #     dd[]
    # print(og)
    # print(b)
    for i in range(len(og)):
        dd[og[i][1]] = b[i]
    
    # print(dd)
    ans = [0 for _ in range(len(og))]
    # print(ans)
    for i in range(len(og)):
        ans[i] = dd[i]
    # for i in range(len(og)):
    #     ans.append(dd[arr[i]])
    print(*ans)
    # print(ans)
    # print(og)
    # print(b)