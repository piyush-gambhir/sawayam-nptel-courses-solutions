n = int(input())
m = {}
c = [0] * int(1e6 + 1)
d = [0] * int(1e6 + 1)

for _ in range(n):
    a, b = map(int, input().split())
    m[a] = b
    c[a] = 1
    d[b] = 1

ans = [0] * n
ans[1] = m[0]

i = 3
while i < n:
    ans[i] = m[ans[i-2]]
    i += 2

temp = None
for i in range(1, int(1e6)):
    if c[i] and not d[i]:
        temp = i
        break

ans[0] = temp
i = 2
while i < n:
    ans[i] = m[ans[i-2]]
    i += 2

print(' '.join(map(str, ans)), end='')
