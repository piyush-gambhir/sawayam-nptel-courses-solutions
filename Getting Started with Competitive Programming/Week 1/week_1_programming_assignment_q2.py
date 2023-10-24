n, m, s, x = map(int, input().split())
vk = [list(map(int, input().split())) for _ in range(n)]

while s > 0:
    p = vk[0][0]
    for i in range(1, m):
        temp = vk[0][i]
        vk[0][i] = p
        p = temp
    for i in range(1, n):
        temp = vk[i][m - 1]
        vk[i][m - 1] = p
        p = temp
    for i in range(m - 2, -1, -1):
        temp = vk[n - 1][i]
        vk[n - 1][i] = p
        p = temp
    for i in range(n - 2, -1, -1):
        temp = vk[i][0]
        vk[i][0] = p
        p = temp
    s -= 1

for i in range(m):
    if (i + x) % x == 0:
        print(vk[0][i], end=" ")
for i in range(1, n):
    if (i + (m - 1) + x) % x == 0:
        print(vk[i][m - 1], end=" ")
for i in range(m - 2, -1, -1):
    if ((n - 1) + i + x) % x == 0:
        print(vk[n - 1][i], end=" ")
for i in range(n - 2, 0, -1):
    if (i + x) % x == 0:
        print(vk[i][0], end=" ")
