t = int(input())
arr = list(map(int, input().split(" ")))
ss = list(sorted(arr))
psa = [0]
psb = [0]
for ind in range( len(arr)):
    psa.append(psa[-1] + arr[ind])
for ind in range(len(arr)):
    psb.append(psb[-1] + ss[ind])

# print(psa)
# print(psb)
n = int(input())
for _ in range(n):
    type, l, r = list(map(int, input().split(" ")))
    if type == 1:
        print(psa[r] - psa[l-1])
    else:
        print(psb[r] - psb[l-1])