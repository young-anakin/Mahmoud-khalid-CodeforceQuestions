t = int(input())
import bisect
for _ in range(t):
    _ = input()
    n, k = list(map(int, input().split(" ")))
    posn = list(map(int, input().split(" ")))
    degree =  list(map(int, input().split(" ")))

    ps = [0 for _ in range(n)]

    prefix = [float("inf") for _ in range(n)]
    suffix = [float("inf") for _ in range(n)]
    # for i in range(n):
    #     prefix[i] =
    for i in range(k):
        ps[posn[i]-1] = degree[i]
    # print(ps)

    mn = 0
    mnVal , mnPos = 0,0

    for i in range(n):
        if ps[i] > 0:
            mnVal = ps[i]
            mnPos = i
            break
    



    # print(mnVal, mnPos)
    for i in range(len(prefix)):
        if ps[i] == 0:
            pass
        else:
            if ps[i] <= mnVal + abs(mnPos - i):
                mnVal, mnPos = ps[i], i
        
        prefix[i] = mnVal + abs(mnPos - i)
    
    last = n-1
    rev = ps[::-1]
    for i in range(n):
        if rev[i] > 0:
            mnVal = rev[i]
            mnPos = i
            break
    
    mnPos = (n - i)-1
    # print(mnVal, mnPos)
    n -=1
    while n >= 0:
        if ps[n] == 0:
            pass
        else:
            if ps[n] <= mnVal + abs(mnPos - n):
                mnVal, mnPos = ps[n], n
        
        suffix[n] = mnVal + abs(mnPos - n)
        n-=1
    # print(prefix)

    ans = []
    # print(suffix)
    # print(prefix)
    for i in range(len(suffix)):
        ans.append(min(suffix[i], prefix[i]))
    
    print(*ans)
    # print(suffix)
    # print(prefix)


