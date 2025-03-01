t = int(input())
for _ in range(t):
    val = input()
    p = "po"
    j = "desu"
    j1 = "masu"
    k = "mnida"

    p, j, j1, k = p[::-1], j[::-1], j1[::-1], k[::-1]

    val = val[::-1]
    check = ""
    for i in val:
        check += i
        if check == p:
            print("FILIPINO")
            break
        elif check == j1 or check == j:
            print("JAPANESE")
            break
        elif check == k:
            print('KOREAN')
            break
        
