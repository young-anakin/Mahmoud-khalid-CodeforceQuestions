t = int(input())
for _ in range(t):
    n, k, p = map(int, input().split())

    if abs(k) > n * p:
        print(-1)
        continue

    if k == 0:
        print(0)
        continue


    min_moves = (abs(k) + p - 1) // p  

    if min_moves > n:
        print(-1)
    else:
        print(min_moves)
