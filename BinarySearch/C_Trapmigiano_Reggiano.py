t = int(input())
from collections import defaultdict, deque
for _ in range(t):
    n, st, en = list(map(int, input().split(" ")))
    graph = defaultdict(list)
    for _ in range(n-1):
        a, b = list(map(int, input().split(" ")))
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()

    queue = deque()
    queue.append(en)
    ans = []
    while queue:
        val = queue.popleft()
        visited.add(val)
        ans.append(val)
        for i in graph[val]:
            if i not in visited:
                queue.append(i)
    
    print(*ans[::-1])
    
