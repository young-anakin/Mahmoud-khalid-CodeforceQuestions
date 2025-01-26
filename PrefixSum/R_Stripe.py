t = int(input())
arr = list(map(int, input().split(" ")))
prefix = []
suffix = []
last = 0
for ind in range(t):
    last += arr[ind]
    prefix.append(last)
last = 0
for ind in range(t-1, -1, -1):
    last += arr[ind]
    suffix.append(last)

suffix = suffix[::-1]
# print(prefix)
# print(suffix)
cp = 0
for ind in range(len(prefix)-1):
    if prefix[ind] == suffix[ind+1]:
        cp +=1

print(cp)
# for ind in range(len())