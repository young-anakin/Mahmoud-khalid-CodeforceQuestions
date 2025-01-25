val = input()
t = int(input())
ps = [0]
ps2 = [0]
for ind in range(1, len(val)):
    if val[ind] == val[ind-1]:
        ps.append(ps[-1] + 1)
    else:
        ps.append(ps[-1])
# print(ps)
for _ in range(t):

    # for ind in range(len(val)):
    #     if val[ind] == val[ind+1]:
    #         ps2.append(ps2[-1] + 1)
    #     else:
    #         ps2.append()

    u, v = list(map(int, input().split(" ")))
    print(abs(ps[u-1] - ps[v-1]))