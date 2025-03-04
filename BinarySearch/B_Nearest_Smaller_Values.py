n = int(input())
arr = list(map(int, input().split()))

stack = []
ans = []
for ind in range(n):
    if not stack:
        ans.append(0)
        stack.append((arr[ind], ind+1))
    else:
        fl = False
        while stack:
            if stack[-1][0] < arr[ind]:
                ans.append(stack[-1][1])
                stack.append((arr[ind], ind+1))
                break
            else:
                stack.pop()
        
        if not stack:
            stack.append((arr[ind], ind+1))
            ans.append(0)

print(*ans)