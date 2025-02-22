t = int(input())
def comp(n, k):
    diff = k
    yalut = k - (k // n)
    curr = k
    while yalut < k:
        x = diff // n
        curr += x 
        yalut += (x + 1 - ((x + 1) // n))
        diff = x + 1
    
    return curr


for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    ans = comp(n, k)
    print(ans)
    

