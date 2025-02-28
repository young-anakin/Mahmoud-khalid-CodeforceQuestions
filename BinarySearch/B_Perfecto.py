import heapq
t = int(input())
import math

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

for _ in range(t):
    n = int(input())
    sm = (n * (n+1))/2
    if is_perfect_square(int(sm)):
        print(-1)
    else:
        ans = []
        sequence = [i for i in range(1, n+1)]
        # print(sequence)
        heap = sequence
        heapq.heapify(sequence)
        # print(heap)
        rs = 0
        while heap:
            val = heapq.heappop(heap)
            rs += val
            # print(val)
            if is_perfect_square(rs):
                t = heapq.heappop(heap)
                ans.append(t)
                heapq.heappush(heap, val)
                rs -= val
                rs += t
            else:
                ans.append(val)
        
        print(*ans)
        # fl = False
        # rs  =0
        # for i in ans:
        #     rs += i
        #     if is_perfect_square(rs):
        #         fl = True
        
        # print(fl)
        # print("ya")

