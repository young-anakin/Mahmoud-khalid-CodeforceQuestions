t = int(input())
from collections import defaultdict
dd = defaultdict()
cp = 0
birth = []
death = []
for _ in range(t):
    a, b = list(map(int, input().split(" ")))
    birth.append((a, 0))
    birth.append((b, 1))
    # death.append(b)
    # arr = []
    # for _ in range(len(arr)):

y, mx = 0 , 0
# for i in range()
birth.sort()
# print(birth)
ans = defaultdict(int)
for i in range(len(birth)):
    if birth[i][1] == 0:
        cp +=1
    else:
        cp -=1
    
    ans[birth[i][0]] = cp
    # if cp > mx:
    #     y = birth[i][0]
    #     mx = cp
    
    # print(cp)
curr = 0
for key, val in ans.items():
    if val > curr:
        y = key
        mx = val
        curr = max(curr, mx)
print(y, mx)


# print(death)