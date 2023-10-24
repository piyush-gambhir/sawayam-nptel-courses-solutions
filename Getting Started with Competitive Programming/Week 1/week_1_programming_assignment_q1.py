t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    vk = list(map(int, input().split()))
    lm = list(map(int, input().split()))
    i, j = 0, 0
    while i < n and j < m:
        if vk[i] == lm[j]:
            vk[i] = 0
            lm[j] = 0
            i += 1
            j += 1
        elif vk[i] > lm[j]:
            vk[i] -= lm[j]
            j += 1
        else:
            lm[j] -= vk[i]
            i += 1
    if i == n and j == m:
        print("Draw")
    elif i == n:
        cost = sum(lm[j:])
        if cost > 0:
            print("Duryodhana")
        else:
            print("Draw")
    else:
        cost = sum(vk[i:])
        if cost > 0:
            print("Yudhisthira")
        else:
            print("Draw")
