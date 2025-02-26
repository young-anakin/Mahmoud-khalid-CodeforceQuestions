t = int(input())
for _ in range(t):
    size, target = map(int, input().split())
    mask = num = 0
    result = []

    while mask | num <= target and num < size:
        result.append(num)
        mask |= num
        num += 1

    index = 0
    while len(result) < size:
        if index == num:
            index = 0
        result.append(index)
        index += 1

    check = 0
    for num in result:
        check |= num  

    if check != target:
        flag = 0
        for i in range(len(result)):
            if result[i] | target > target:
                result[i] = target 
                flag = 1

        if not flag:
            result[-1] = target   

    print(*result)

