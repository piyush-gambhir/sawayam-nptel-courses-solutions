def bisect_left(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def add_lower(L, k):
    if not L:
        L.append(k)
        return L

    index = bisect_left(L, k)
    if index == len(L):
        L.append(k)
    else:
        L[index] = k
    return L


n = int(input())
a = list(map(int, input().split()))
L = []
for i in a:
    add_lower(L, i)
print(len(L))
