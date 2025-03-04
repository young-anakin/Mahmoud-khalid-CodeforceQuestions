t = int(input())
import math
for _ in range(t):
    n, x = list(map(int, input().split(" "))) # Types of blows and 
    ans = float("INF")
    mx = -1
    md, mh = 0,0
    for _ in range(n):
        d, h = list(map(int, input().split(" ")))
        if d - h > 0:
            if d-h > mx:
                mx = max(mx, d-h)
                md, mh = d, h
        
    
    if mx == -1:
        print(-1)
    else:
        print((x + mx)// (mx+1))
        # pass
    # print(mx, md, mh)
