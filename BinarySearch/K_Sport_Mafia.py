n, k = list(map(int, input().split(" ")))
candies = [1]
# if I ate 5 rounds, that means I have eaten 15 candies. My overall candies are 11, so that means 
# i have to have eaten 4 candies
def check(curr, n):
    overallCandies = (curr * (curr+1))//2
    movesLeft = n - curr

    return overallCandies - movesLeft

# print()
def binarySearch(l, r, n, k):
    while l <= r:
        md = (l + r)//2
        # print(md)
        if check(md, n) == k:
            return n - md
        elif check(md, n) > k:
            r = md-1
        else:
            l = md+1
print(binarySearch(1, 10**9, n, k))