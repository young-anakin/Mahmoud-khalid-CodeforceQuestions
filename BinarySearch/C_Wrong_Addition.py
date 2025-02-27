t = int(input())
for _ in range(t):
    a, c = list(map(str, input().split(" ")))
    a = a[::-1]
    c = c[::-1]
    j = 0
    bucket = []
    for z in range(len(a)):
        i = a[z]
        tmp = ""
        if j >= len(c):
            for x in range(z, len(a)):
                bucket.append(a[x])
        tmp += c[j]
        j +=1
        while j < len(c) and int(tmp[::-1]) < int(i):
            tmp += c[j]
            j +=1
        
        bucket.append(abs(int(tmp[::-1]) - int(i)))
        # tmp = ""
        print(tmp[::-1], i)
    
    bucket = bucket[::-1]
    print(bucket)
        

    # print(a, b)