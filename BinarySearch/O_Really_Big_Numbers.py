n, k = list(map(int, input().split(" ")))
def binarySearch(l, r, k):
    while l <= r:
        md = (l+r)//2
        val = 0
        for i in str(md):
            val += int(i)
        
        # val = int(val)
        # print(md-val, md)
        if md - val > k:
            r = md - 1
        elif md - val < k:  
            l = md+1
        else:
            # print("yaaaa")
            return l
        # print(md, l, r)
    
    return l
        
x = binarySearch(1, n, k)
if x > n:
    print(0)
else:
    print(abs(x-n) + 1)
# print(x)