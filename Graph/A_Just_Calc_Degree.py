n = int(input())
arr = []
from collections import defaultdict, deque
graph = defaultdict(list)
isLeaf = defaultdict(bool)
queue = deque()
visited = set()
for ind in range(n-1):
    val = int(input())

    graph[val].append(ind+2)
    # isLeaf[val] = True
    if val not in visited:
        queue.append(val)
        visited.add(val)

# print(graph)
for ind in range(1, n+1):
    if len(graph[ind]) == 0:
        isLeaf[ind] = True
    else:
        isLeaf[ind] = False

ans = False
children = defaultdict(int)
# print(queue)
while queue:
    val = queue.popleft()
    for ind in graph[val]:
        # print(val, ind, isLeaf[ind])
        if isLeaf[ind] == True:
            children[val] +=1
        else:
            children[val] += 0
        if ind not in visited and graph[ind]:
            queue.append(ind)
# pri/nt(children)
fl = True
for key, val in children.items():
    if val < 3:
        fl = False
        break

if fl:
    print("YES")
else:
    print("NO")
