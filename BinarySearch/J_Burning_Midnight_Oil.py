n, k = list(map(int, input().split(" ")))

def calculate(val, k):
    sm = 0
    # k = 
    while val != 0:
        sm += val
        val = val//k
    
    return sm

mn = 1
mx = 10**9
ans = float("inf")
# print(calculate(4, k))
while mn <= mx:
    md = (mn + mx)//2
    # print(md, calculate(md, k))
    
    if calculate(md, k) >= n:
        mx = md-1
        ans = min(ans, md)
    else:
        mn = md+1

print(ans)