t = int(input())
for _ in range(t):
    a, c = list(map(str, input().split(" ")))
    a = a[::-1]
    c = c[::-1]
    j = 0
    bucket = []
    for i in a:
        tmp = ""
        if j >= len(c):
            break
        tmp += c[j]
        j +=1
        while j < len(c) and int(tmp[::-1]) < int(i):
            tmp += c[j]
            j +=1
        
        bucket.append(abs(int(tmp[::-1]) - int(i)))
    
    for i in range(j, len(c)):
        bucket.append(int(c[i]))
    b = ""
    for i in bucket:
        i = str(i)[::-1]
        b += str(i)
    

    
    fin = []
    x, y = 0,0
    while x < len(a) or y < len(b):
        if x >= len(a) or y >= len(b):
            if x >= len(a):
                fin += b[y]
            if y >= len(b):
                fin += a[x]
        else:
            fin .append(str(int(b[y]) + int(a[x]))[::-1])        
        y +=1
        x +=1

    fin = ("".join(fin)[::-1])
    # print(fin)
    c = c[::-1]
    if fin == c:
        b = b[::-1]
        b = b.lstrip('0')
        print(b)
    else:
        print(-1)
    

