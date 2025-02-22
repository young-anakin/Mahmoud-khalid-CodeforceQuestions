t = int(input())
def checker(arr):
    return arr[0][0] < arr[0][1] and arr[1][0] < arr[1][1] and arr[0][0] < arr[1][0] and arr[0][1] < arr[1][1] 
for _ in range(t):
    a, b = list(map(int, input().split(" ")))
    c, d = list(map(int, input().split(" ")))

    if checker([[a,b], [c,d]]) or checker([[c, a], [d, b]]) or checker([[d, c], [b, a]]) or checker([[b, d], [a, c]]):
        print("YES")
    else:
        print("NO")

