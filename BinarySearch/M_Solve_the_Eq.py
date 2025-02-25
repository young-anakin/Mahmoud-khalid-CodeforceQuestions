t = int(input())
def binarySearch(n):
    l = 1
    r = 10 ** 12
 
    while l < r:
        md = (l+r)//2
 
        firstAdded = md / (10 ** 12)
        secondAdded = 1 - firstAdded
        ans = (((n - 2) + secondAdded) * (1 + firstAdded))
        # print((n - 2) + firstAdded, 1+secondAdded  )
        # print(firstAdded , secondAdded, ans)
        # print(ans * (10 ** 6) , n * (10 ** 6))
        if int(ans * (10 ** 6)) == n * (10 ** 6):
            return (True, ((n - 2) + secondAdded, 1+firstAdded ))
        elif ans < n:
            l = md + 1
        elif ans > n:
            r = md -1
    return (False, -1)
 
for i in range(t):
    n = int(input())
    if n == 0:
        print("Y", 0.0000, 0.00000)
    else:
        # if 
        a, b = binarySearch(n)
        # print(a, b)
        if a == False:
            print("N")
        else:
            print("Y", b[0], b[1])