t = int(input())
def integer_cube_root(x):
    if x < 0:
        return None  # Handle negative numbers as needed
    lo, hi = 0, x
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_cubed = mid * mid * mid
        if mid_cubed == x:
            return mid
        elif mid_cubed < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo - 1  # Return the floor of the cube root

    
 
for _ in range(t):
    n = int(input())
    i = 1
    fl = False
    while i ** 3 < n:
        firstNum = i ** 3
        secondNum = n - firstNum

        if secondNum == integer_cube_root(secondNum) ** 3:
            fl = True
            break
        i +=1
    if fl:
        print("YES")
    else:
        print("NO")
