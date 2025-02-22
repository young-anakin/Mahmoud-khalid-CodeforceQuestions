n, m , k = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
prefix = [0] * n
operations = []
print(prefix)
for _ in range(m):
    l, r, d = list(map(int, input().split(" ")))
    operations.append((l,r,d))

for _ in range(k):
    a, b = list(map(int, input().split(" ")))
    first = operations[a-1]
    second = operations[b   ]
print(operations)