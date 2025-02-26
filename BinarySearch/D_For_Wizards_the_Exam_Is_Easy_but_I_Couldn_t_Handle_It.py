t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))

    checker = []

    greater = []

    for i in range(len(arr)):
        cp = 0
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                cp +=1
        
        greater.append(cp)
    # print(greater)
    already = sum(greater)
    mx = already
    a, b = 0,0
    for i in range(len(arr)):
        curr = already
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                curr -=1
            elif arr[i] < arr[j]:
                curr +=1
            
            if curr < mx:
                a, b = i, j
                mx = min(mx, curr)
            
    
    print(a+1, b+1)
    # print(mx)