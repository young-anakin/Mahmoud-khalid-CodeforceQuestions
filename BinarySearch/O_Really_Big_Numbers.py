n, k = list(map(int, input().split(" ")))
def binarySearch(l, r, k):
    while l < r:
        md = (l+r)//2
        val = 0
        for i in str(md):
            val += int(i)
        
        # val = int(val)
        if md - val > k:
            r -=1
        elif md - val < k:
            l +=1
        else:
            return x
        print(md, l, r)
    
    return r
        
x = binarySearch(1, n, k)
print(x)